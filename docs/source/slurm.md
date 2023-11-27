# Slurm

COSMA has a set of integrated batch queues that are managed by Slurm Workload Manager job scheduler. Jobs are ran by the scheduler after submission to the appropriate queue. Which queue to submit your jobs to depends on the projects you are working on, if in doubt about this ask your project lead, supervisor, co-workers or email cosma-support@durham.ac.uk.

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

Example submission script examples can be found in the ```/cosma/home/sample-user``` directory.

Read more:

* ```man slrum```, ```man sbatch```, etc. [online version](https://slurm.schedmd.com/man_index.html).
* [cheatsheet](https://slurm.schedmd.com/pdfs/summary.pdf)
* [Rosetta stone of batch systems](https://slurm.schedmd.com/rosetta.pdf) (for users coming from other systems, such as LSF)

Jobs, except for those in the *-princes family of queues are limited to a maximum runtime of 72 hours. If your job will take significantly less than this, then it is recommended to insert the expected runtime, as this may enable the job to be scheduled earlier.

Some hints and tips for using SLURM can be found [here](LINK).

## X11 forwarding for debugging

If is possible to forward a display for debugging and profiling purposes (e.g. to use a graphical profiler). For example:

`srun -p cosma7 -A dp004 -t 0:02:00 --x11 --pty /bin/bash`

Once you get a prompt on the node you run standard X11 applications.

## Direct compute node access

For direct compute access, you can use srun, e.g.:

`srun -p cosma7 -A dpXXX -n 1 -t 1:00:00 --pty /bin/bash`

[Performance co-pilot] (LINK) will also allow you to analyse running jobs.

Should you need direct ssh access to a node running your jobs, this may be possible - please contact cosma-support.

## Example scripts

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

### Using the cordelia queue to submit single core jobs without taking up a whole node

Use:

    #SBATCH -n 1

    #SBATCH -p cordelia

    #SBATCH --cpu-per-task=1

    #SBATCH --mem-per-cpu=4096

    (and other standard options)

Cordelia is a shared queue, so multiple users run jobs simultaneously on these nodes.

The cosma7-shm queue can also be used for large memory requirements. These are single nodes, though not exclusive (i.e. multiple user jobs can run simultaneously).

### Using DDT without direct compute node access

To use DDT with slurm, the following instructions can be followed:

https://gitlab.cosma.dur.ac.uk/swift/swiftsim/wikis/DDT-debugger-on-Cosma
