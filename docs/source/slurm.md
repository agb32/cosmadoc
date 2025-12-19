# Slurm

COSMA has a set of integrated batch queues that are managed by Slurm Workload Manager job scheduler. Jobs are ran by the scheduler after submission to the appropriate queue. Which queue to submit your jobs to depends on the projects you are working on, if in doubt about this ask your project lead, supervisor, co-workers or email cosma-support@durham.ac.uk.  For a more indepth discussion of job priorities and how Slurm is configured, please see [here](slurmdetail.md)

Common commands:

* ```sbatch my_scriptc.sh```: submits my_scripts.sh to the queue. Job configuration can be done by command-line flags
* ```scancel 12345678```: cancels job number 12345678
* ```squeue -u $USER```: displays currently running jobs submitted by $USER
* ```squeue -p $QUEUE```: displays jobs currently running in $QUEUE
* ```sinfo -s```: displays summary of queues
* ```srun```: start a terminal on a single node
* ```salloc```: starts a new environment which can be used to launch mpi jobs
* ```showq [-q cosma7] [-f] [-h]```: displays additional information about queues
* ```sshare```: show the share/priorities of the queue
* ```slurmnodeprop```: summarise the properties of nodes or queues (use -h for more details)
* ```sreport```: report on usage

Example submission script examples can be found in the ```/cosma/home/sample-user``` directory.

Read more:

* ```man slrum```, ```man sbatch```, etc. [online version](https://slurm.schedmd.com/man_index.html).
* [cheatsheet](https://slurm.schedmd.com/pdfs/summary.pdf)
* [Rosetta stone of batch systems](https://slurm.schedmd.com/rosetta.pdf) (for users coming from other systems, such as LSF)

Jobs, except for those in the *-princes family of queues are limited to a maximum runtime of 72 hours. If your job will take significantly less than this, then it is recommended to insert the expected runtime, as this may enable the job to be scheduled earlier.

Some hints and tips for using SLURM can be found [here](slurm.md#slurm-hints-and-tips).

## X11 forwarding for debugging

If is possible to forward a display for debugging and profiling purposes (e.g. to use a graphical profiler). For example:

`srun -p cosma7 -A dp004 -t 0:02:00 --x11 --pty /bin/bash`

Once you get a prompt on the node you run standard X11 applications.

## Direct compute node access

For direct compute access, you can use srun, e.g.:

`srun -p cosma7 -A dpXXX -n 1 -t 1:00:00 --pty /bin/bash`

[Performance co-pilot](system.md#performance-co-pilot) will also allow you to analyse running jobs.

Should you need direct ssh access to a node running your jobs, this may be possible - please contact cosma-support.

## Reservations

It is possible to request a SLURM reservation for jobs that will require around 40% or more of the cluster simultaneously.  A reservation sets aside the requested number of nodes for a set period of time for exclusive use, allowing large jobs to restart efficiently, without having to join the back of a queue and wait for a large number of nodes to drain.  This improves cluster efficiency.

A reservation request needs to be authorised by the Service Management Board, and 1 month notice should be given if possible.  The request should detail how many nodes are required (we will add a few more in case of node failures), for how long, a brief description of the science, and why the reservation is required.

It should be noted that your project will be charged for the entire reservation, not just for the time you use.  Therefore it is essential to make sure that you maintain a queue of jobs in the reservation queue.

Once you have been given a reservation, you can use the `scontrol show reservation` command to view the reservation, and submit jobs to it using the `#SBATCH --reservation=RESERVATION NAME` flag in your submission script.

## HDF5 profiling

The [SLURM HDF5 profiling plugin](https://slurm.schedmd.com/hdf5_profile_user_guide.html) is enabled, allowing profiling information from a given job to be catured in a HDF5 file.  Results are stored within `/cosma/apps/slurm/profile_data/USERNAME`.  To enable this, you should specify the `#SBATCH --profile=<all|none|energy|task|filesystem|network>` options within your batch script.  The node-step files are merged into one HDF5 file per job.

After the job has finished, you can run `sh5util -j JOBID` to concatenate all the files created by the job (one per node) into a single file in the current directory.  You can then use the `h5ls` command (part of the hdf5 module) to view the contents of the file on the commandline.

## Example scripts and command usage

### Large job over many nodes

    #!/bin/bash -l

    #SBATCH --ntasks 512 # The number of cores you need...
    #SBATCH -J job_name #Give it something meaningful.
    #SBATCH -o standard_output_file.%J.out
    #SBATCH -e standard_error_file.%J.err
    #SBATCH -p cosma7 #or some other partition, e.g. cosma, cosma8, etc.
    #SBATCH -A project #e.g. dp004
    #SBATCH --exclusive
    #SBATCH -t 72:00:00
    #SBATCH --mail-type=END # notifications for job done &
    fail
    #SBATCH --mail-user=<email address> #PLEASE PUT YOUR EMAIL ADDRESS HERE (without the <>)

    module purge
    #load the modules used to build your program.
    module load intel_comp
    module load intel_mpi
    module load hdf5


    #Run the program
    mpirun -np $SLURM_NTASKS your_program your_inputs

### Many similar jobs simultaneously

    #!/bin/bash -l

    #SBATCH --ntasks 512
    #SBATCH -J job_name
    #SBATCH --array=1-28 #Run 28 copies of the code
    #SBATCH -o standard_output_file.%A.%a.out
    #SBATCH -e standard_error_file.%A.%a.err
    #SBATCH -p cosma7
    #SBATCH -A project
    #SBATCH --exclusive
    #SBATCH -t 72:00:00
    #SBATCH --mail-type=END # notifications for job done & fail
    #SBATCH --mail-user=<email address>

    module purge
    #load the modules used to build your program.
    module load intel_comp
    module load intel_mpi
    module load hdf5

    #Run the program, note $SLURM_ARRAY_TASK_ID is set to the array number.

    mpirun -np $SLURM_NTASKS your_program your_inputs $SLURM_ARRAY_TASK_ID

### Many single core jobs on a single node

See the example in `/cosma/home/sample-user/parallel_tasks/`

(copy this to your own directory, compile the c code (`make`), and edit the `slurm_batch.sh` file.

### Many nodes with 2 jobs per node (which can then make use of the additional cores using threading/OPENMP)

Specify the total number of MPI tasks (e.g. to run on 4 nodes):

    #SBATCH --ntasks=8

And specify the number of cores per task:

For COSMA7 (28 cores per node):

    #SBATCH --cpus-per-task=14

For COSMA5 (16 cores per node):

    #SBATCH --cpus-per-task=8

    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

### Using non-uniform resources per node in a single job (heterogenous jobs)

Slurm allows requesting multiple node configurations in one batch submission:

    #SBATCH -A project
    #SBATCH --time=72:00:00
    
    #SBATCH -p cosma8
    #SBATCH --nodes=1
    #SBATCH --tasks-per-node=1

    #SBATCH hetjob

    #SBATCH -p cosma8
    #SBATCH --nodes=2
    #SBATCH --tasks-per-node=8

This example requests one node where one task will run and two additional nodes where a total of 16 tasks will run. Using `sbatch` is often impractical for a heterogenous job, however, because `mpirun` does not understand this kind of resource allocation. MPI jobs can instead be started with `srun`, for example:

    salloc -A project --time=72:00:00 -p cosma8 --nodes=3
    srun --nodes=1 --tasks-per-node=1 ./server : --nodes=2 --tasks-per-node=8 ./client

This example has the same distribution of tasks as the batch script just above. It starts a server task alone on the first node and then 16 client tasks on the other two nodes. All of the tasks will exist in the same `MPI_COMM_WORLD`.

#### Another example could use:

    #SBATCH -p cosma8
    #SBATCH --ntasks=64
    #SBATCH --tasks-per-node=16
    #SBATCH --distribution=block:fcyclic:fcyclic,Pack

    #SBATCH hetjob

    #SBATCH -p cosma8
    #SBATCH --ntasks=28
    #SBATCH --tasks-per-node=1
    #SBATCH --distribution=cyclic

    mpirun -np 64 ./swift_mpi -v 1 --pin --threads=8 --cosmology  --self-gravity params.yml : \
    -np 28 ./swift_mpi -v 1 --pin --threads=128 --cosmology --self-gravity params.yml

Note, changes to the `--distribution` option may be required.  This example tries to fill each node with tasks before moving to the next one ("block" and "Pack"), and then hand out tasks within a node round-robin among the sockets and cores ("fcyclic").  The slurm documentation has a list of parameters that must be shared between all jobs, those that can be shared or specified individually, andthose that must be specified for each job.

#### Heterogeneous jobs

OpenMPI supports heterogenous jobs, but to use this the MPI installation must be linked against a process management interface (PMI) library. A clear error message seems to be produced when this is missing. Intel MPI implementations seem to work to some extent provided that the environment variable `export I_MPI_PMI_LIBRARY=/usr/lib64/libpmi.so` is set, but it's not clear that heterogenous jobs are fully supported and there seems to be some limitations (such as mixing nodes with exactly 1 and >1 tasks causing a crash) in some cases. Further documentation and examples can be found at [https://slurm.schedmd.com/heterogeneous_jobs.html](https://slurm.schedmd.com/heterogeneous_jobs.html).

### Using DDT without direct compute node access

To use DDT with slurm, the following instructions can be followed:

[https://gitlab.cosma.dur.ac.uk/swift/swiftsim/wikis/DDT-debugger-on-Cosma](https://gitlab.cosma.dur.ac.uk/swift/swiftsim/wikis/DDT-debugger-on-Cosma)

There is also an example Slurm submission script in /cosma/home/sample-user/slurm_ddt_example.qtf which [DDT uses to generate a batch script](issues.md#ddt).  

### SLURM hints and tips

To use fewer than all cores in a node, with a multiple node job, use something like:

(e.g. for cosma6, requiring 256 MPI tasks (but 512 cores), on 32 nodes, so 8 MPI ranks per node - cosma6 has 16 cores per node)

> #SBATCH --ntasks=256
> #SBATCH --cpus-per-task=2


#### Batch Queue priorities

The priority of pending jobs in a queue is determined by a number of factors. These include:

1. How successful the user has previously been at getting time (which is a factor that decays over time)

2. Group fair-share: this can be raised for small groups/projects

It is possible to change the priority of you jobs:

scontrol update job JOBNUMBER nice=100 (which will lower its priority)

#### Queue information

The `showq` command can be used to obtain useful information about the queues (in addition to squeue and sinfo). For example:

```showq -q cosma7 -l -f -o```

The `c7jobload` command will give the load (i.e. CPU demand) of a job. Use -h to see options.  Likewise `c8jobload`, etc.  For example:

```
c8jobload -l JOBID
```


`sinfo -s` will give a succinct overview of the partitions.

The `sstat` (for running jobs) and `sacct` (for completed jobs) provide information about the jobs. For example, at the end of your batch script, if you use:

```sstat --jobs=${SLURM_JOBID}.batch --format=jobid,maxrss,ntasks```

it will print information about memory used.

### Reporting using sreport

e.g.

```
sreport cluster AccountUtilizationByUser start=mmdd end=mmdd Account=dpXXX
```
