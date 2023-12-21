# Code-specific information

See the below for known hints and issues related to certain codes. These may give compilation hints, execution hints, etc.

It should be noted that highly optimised code compiled on COSMA7 may not run on COSMA5 since these CPU architectures are older, and have a reduced instruction set, or on COSMA8, which does not support AVX512 instructions.. Therefore, if you need code to run on COSMA5, and are suffering from "illegal instructions", please try recompiling on COSMA5. Likewise, to run code on COSMA8, please compile on a COSMA8 login node.

## SWIFT

A specific page for [SWIFT](swift.md) exists.

## GADGET3

From Rob Crain:

Since the switch to intel mpi 2018, I've found a repeatable hang in a GADGET3 run with a particular set of ICs. I traced this to a call of MPI_Allgather in mymalloc.c. Note this is *not* the MPI_Allgatherv call where intel mpi gripes over the in-place issue. I found that 64 of 128 tasks returned from the operation fine, and the results stored in their output array were what I expected (which of course requires that *all* of the NTasks successfully communicate), so I am still at a loss as to why this happens.

However out of desperation I tried manually fixing which gather algorithm the routine uses (normally it picks from up to 5 depending on the message size and number). I quickly tried forcing to each one and got a mixed bag of results, which weren't entirely repeatable. But using method 1 (recursive doubling) seems to have resolved the issue (watch this space). To do this I added the following to my slurm script:

    export I_MPI_ADJUST_ALLGATHER=1

### Other solutions

Illegal MPI call in forcetree.c

Gadget contains an MPI_Allgatherv call where the input and output buffers overlap. This is not allowed by the MPI standard. Intel MPI detects this error and stops the program with a message about aliased buffers. E.g.:

    Fatal error in PMPI_Allgatherv: Invalid buffer pointer, error stack:
    PMPI_Allgatherv(1452): MPI_Allgatherv(sbuf=0x2b6383018c14, scount=352, 
    MPI_BYTE, rbuf=0x2b6383016568, rcounts=0x2b6383042568, displs=0x2b63830425e8,
    MPI_BYTE, MPI_COMM_WORLD) failed 

This can be fixed by changing the following line in forcetree.c from

    MPI_Allgatherv(&DomainMoment[DomainStartList[ThisTask * MULTIPLEDOMAINS + m]], recvcounts[ThisTask],
    MPI_BYTE, &DomainMoment[0], recvcounts, recvoffset, MPI_BYTE, MPI_COMM_WORLD);

to

    MPI_Allgatherv(MPI_IN_PLACE, recvcounts[ThisTask],
    MPI_BYTE, &DomainMoment[0], recvcounts, recvoffset, MPI_BYTE, MPI_COMM_WORLD);

Some versions of Gadget have a preprocessor macro which can be enabled to make this change 
(e.g. `USE_MPI_IN_PLACE`, or `FIX_FOR_BLUEGENE_MPI`).

### Crashes due to MaxMemSize too large

n the Gadget parameter file there is a parameter MaxMemSize which specifies how much memory Gadget should use. Gadget allocates MaxMemSize megabytes of memory on each MPI task at startup. Setting this value too high leaves no memory for MPI to use and will cause runs to crash with various internal MPI errors.

On larger runs MaxMemSize may need to be no more than about 70% of the memory available to each core. MaxMemSize=16500 seems to be a reasonable choice on Cosma-7 when using Intel MPI.

### Limits on MPI message sizes

The MPI interface limits messages to (2**31)-1 elements on systems with 32 bit ints. Additionally, some MPI implementations fail if the total size of a message is more than 2Gb.

Some versions of Gadget contain preprocessor macros to limit message sizes. These should be set to some value < 2000 in either the Makefile or Config.sh. E.g.

    MPI_SIZELIMIT=400

and/or

    MPISENDRECV_SIZELIMIT=400

depending on the version of Gadget. Some older versions of Gadget have neither of these options and will need to be updated before they will work with large numbers of particles on each MPI task.

### Intel MPI issue with large messages

Messages >2Gb can cause problems with Intel MPI. The workaround is to set the following environment variables in your batch script:

    export I_MPI_DAPL_CHECK_MAX_RDMA_SIZE=enable
    export I_MPI_DAPL_MAX_MSG_SIZE=1073741824

### HDF5 library version

Gadget (at least up to Gadget-3) uses the HDF5 1.6 API. Cosma-7 only has HDF5 1.8 and 1.10 libraries installed, so Gadget should be compiled with the compatibility macro H5_USE_16_API enabled - i.e. add -DH5_USE_16_API to the compiler flags.

### Gadget3 type codes : how to for intel

If you allocate more than 70% of the available RAM/per core in MaxMemSize, your code might crash with strange MPI errors. On COSMA7, please allocate no more than 20000 MB:

    MaxMemSize 20000

If you are using the same buffer for INPUT and OUTPUT in MPI_Allgatherv, then you will have to use MPI_USE_INPLACE in the MPI_Allgatherv call.

It is also advised to use

    I_MPI_DAPL_CHECK_MAX_RDMA_SIZE=enable
    I_MPI_DAPL_MAX_MSG_SIZE=1073741824

which you can do in a commandline instruction as

    mpirun -genv I_MPI_DAPL_CHECK_MAX_RDMA_SIZE=enable -genv
    I_MPI_DAPL_MAX_MSG_SIZE=1073741824 -n number-of-slots ....

As the interconnect is Mellanox Infiniband it is highly recommended to pin the processes, as a minimum with the options:

    I_MPI_PIN=on
    I_MPI_PIN_MODE=pm

### Gadget-3/GIZMO on COSMA8

The following has been found to work with GIZMO (Romeel Dave):

    module load intel_comp/2021.3.0 compiler mpi
    module load ucx/1.10.1
    module load fftw/3.3.9epyc
    module load gsl
    module load hdf5/1.12.0export HDF5_DISABLE_VERSION_CHECK=1

## DDT

When using the allinea/ddt/18.2.1 module, for reference, users need to specify the file:

    /cosma/local/arm/ddt/18.2.1/templates/slurm.qtf

in the "template file" field of the job submission settings. They also need to set the submission
command to

`sbatch --exclusive -A dp004`

and then

cosma7

in the queue parameters.

## Python issues

### Matplotlib

Matplotlib hanging, during a call to fork()? Try setting environment variable `KMP_INIT_AT_FORK=FALSE`

This could be caused by a bug in the Intel openmp library.

### h5py

Getting the following message when importing h5py?


    --------------------------------------------------------------------------
    A process has executed an operation involving a call to the
    "fork()" system call to create a child process.  Open MPI is currently
    operating in a condition that could result in memory corruption or
    other system errors; your job may hang, crash, or produce silent
    data corruption.  The use of fork() (or system() or other calls that
    create child processes) is strongly discouraged.

    The process that invoked fork was:

    Local host:          [[8264,1],0] (PID 203173)

    If you are *absolutely sure* that your application will successfully
    and correctly survive a call to fork(), you may disable this warning
    by setting the mpi_warn_on_fork MCA parameter to 0.
    --------------------------------------------------------------------------

We think it is harmless, so just ignore it.

## BAM

Ed Fauchon-Jones, June 2019

We had been trying since the beginning of March to run on COSMA7, with most runs resulting in failures. Here is a summary of our attempts to solve this issue.

* We have tried with two versions of our code
Both versions of our code have been used successfully on COSMA5 and COSMA6
hardware.

* Using multiple compiler/MPI library combinations
We have tried to build our code using the following compiler and MPI library
combinations. All jobs failed using these combinations.
* gnu_comp/7.3.0, openmpi/3.0.1
* intel_comp/2018, intel_mpi/2018 (used successfully on COSMA6
hardware)
* intel_comp/2019-update2, intel_mpi/2019-update2

* Different compiler options
We tried with different levels of compiler optimisation and including and
excluding debugging information, all leading to failures.

* Non-actionable and inconsistent errors
Errors are not usually reproducible when running identical jobs, and
typically fail with different errors. Unfortunately the error messages never
provided enough actionable information to find solutions and no one
including our resident research software engineer were able to find a
solution at the time.

* Non-actionable instrumented runs
We also performed some instrumented runs including AddressSanitizer to
attempt to debug our code. We would no longer get failures with the
instrumented code however this would result in much worse performance.

Based on the results it suggested the issue was with our code rather than
COSMA7 or software modules.

In early May we used the newly available openmpi/20190429 module along side
gnu_comp/7.3.0.<http://7.3.0.> This particular combination worked. Based on
the previous failure results we believe the issue we had with the OpenMPI
library was related to https://github.com/open-mpi/ompi/issues/4686 and was
solved with https://github.com/open-mpi/ompi/pull/4767 which was not
available in any of the OpenMPI modules previously available for COSMA7.

## covid-sim

The UCL Pandemic modelling tool used for modelling COVID-19. This is available from https://github.com/mrc-ide/covid-sim/

Installation: you will need a compiler module, the cmake module and python3.

So, e.g. `module load gnu_comp/9.3.0 python/3.6.5 cmake`

This is a cmake build process:

    mkdir build
    cd build
    cmake ../src
    make

If using the Intel compiler, the following options can be used:

    cmake -DCMAKE_CXX_COMPILER:FILEPATH=icpc DCMAKE_CXX_FLAGS:STRING="-O3 -no-prec-sqrt -no-prec-div -fp-model fast=2 -xAVX" -DOpenMP_CXX_FLAGS:STRING="-qopenmp" -DCMAKE_C_COMPILER:FILEPATH=icc -DCMAKE_C_FLAGS:STRING="-O3 -no-prec-sqrt -no-prec-div -fp-model fast=2 -xAVX" -DOpenMP_C_FLAGS:STRING="-qopenmp" -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -DCOUNTRY:STRING=UK -DUSE_OPENMP:BOOL=ON ../src/

The regression test in tests/ will attempt to compile its own version of the code, e.g. when you run:

    python3 regressiontest_UK_100th.py

To avoid this, edit the file and replace the subprocess.check_call lines that call cmake with something appropriate (e.g. nothing, or a cp if copying your CovidSim from elsewhere)

### Running

Once you have compiled the code, you can run it using the data/run_sample.py script.

    python3 run_sample.py --covidsim=../build/CovidSim --datadir=./ --paramdir=param_files/ --outputdir=outputdir United_Kingdom

Batch script:

    #!/bin/bash -l
    #SBATCH --ntasks 16
    #SBATCH -J covidsim
    #SBATCH -o slurmout%J.txt
    #SBATCH -e slurmerr%J.txt
    #SBATCH -p cosma
    #SBATCH -A durham
    #SBATCH --exclusive
    #SBATCH -t 1:00:00
    #SBATCH --mail-type=END
    #SBATCH --mail-user=your.email@here
    module purge#load the modules used to build your program.
    module load intel_comp
    module load python/3.6.5
    module load cmake
    cd data
    python3 run_sample.py --covidsim=../build/CovidSim --datadir=./ --paramdir=param_files/ --outputdir=outputdir United_Kingdom

## paraview

To launch paraview, use:

    module load paraview/...

    paraview --mesa

## GADGET4

GADGET 4 on COSMA8

For the large 274 node commissioning runs, the following settings were used:

    module load gnu_comp/9.3.0
    module load openmpi/4.1.1
    module load gsl/2.4

with the settings:

    export UCX_TLS=self,sm,ud
    export UCX_UD_MLX5_RX_QUEUE_LEN=16384

If writing restart files, it is also important to get striping correct, depending on whether you are using /snap8 (ideally), or /cosma8. This can make a huge difference to runtimes. Please ask if you are unsure.

## Rockstar

To take advantage of Rockstar parallelisation features on the shared-memory queues cosma7-shm and cosma8-shm (or on a single cosma7/cosma8
node) in your SBATCH script set —ntasks=1 and —cpus-per-task=<# of processes=NUM_BLOCKS+NUM_WRITERS>. 

The maximum number of CPUs that can be allocated depends on the specific queue used for your job (e.g. —cpus-per-task<=28 for cosma7). In your Rockstar configuration file set NUM_BLOCKS and NUM_WRITERS=FORK_PROCESSORS_PER_MACHINE to the desired values and run

`./rockstar -c </path/to/configuration file> &`

`sleep 1`

`./rockstar -c [OUTBASE]/auto-rockstar.cfg &`

If running on a single node, you may also wish to set `PARALLEL_IO_SERVER_INTERFACE = lo`
The `PARALLEL_IO` variable must be set to 1.

## COSMOS++

To get Cosmos++ working well on COSMA8, the following parameters were used:

    module load intel_comp/2022.3.0
    module load compiler mpi
    module load hdf5/1.14.0
    module load gsl
    module load python/3.6.5
    export LD_LIBRARY_PATH=/cosma/local/gcc/11.1.0/lib64:$LD_LIBRARY_PATH
