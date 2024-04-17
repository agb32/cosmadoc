# COSMA8

## Using Cosma8

COSMA8 has 2 login nodes, accessed via login8.cosma.dur.ac.uk

COSMA8 has 528 compute nodes, each of which have 1TB RAM and 128 cores (360 are 2x AMD 7H12 processors and 168 are 2x AMD 7763 processors)

There are 2 high RAM (4TB) fat nodes, which should be accessed via the cosma8-shm queue.

There are a number of GPU-enabled servers (see below), a 1TB AMD Milan test node and a 1TB Milan-X test node.

There are 4 relevant SLURM queues:

__cosma8__: provides exclusive access to nodes, shared with cosma8-serial

__cosma8-serial__: provides non-exclusive access to nodes. Use this if you want less than 128 cores (and remember to specify your memory requirement too)

__cosma8-rome__: A subset of cosma8, 360 nodes with Rome processors

__cosma8-milan__: A subset of cosma8, 168 nodes with Milan processors

__cosma8-shm__: access to the mad04 and mad05 servers, with 4TB RAM. These is also non-exclusive, so may be shared with other users if you don't require all 128 cores or all 4TB RAM.

__cosma8-shm2__: access to the ga004 server with a Milan 7703 processor and MI100 GPU.

## Useful information

### Numerical libraries

__OpenBLAS__

OpenBLAS is available via the openblas modules.

__GSL__
The Gnu Scientific Library can be accessed via the gsl modules.

#### Using MKL with COSMA8

MKL: The Intel Math Kernel Library is known to be hobbled on AMD systems. 

MKL is available via the `intel_comp` and `oneAPI` modules.

There is a fix that must be applied: 

By default, MKL (the Intel Math Kernel Library) does not select the best the best options when used on COSMA8, delivering significantly lower performance. For versions of MKL prior to 2020, setting `MKL_DEBUG_CPU_TYPE=5` would force it to use the zen2 code path. However, for newer versions, this no longer works. Instead, the following workaround should be used:

```bash
cat <<EOF > amdmkl.c
int mkl_serv_intel_cpu_true() { return 1; }

EOF
```
    gcc -shared -fPIC -o libamdmkl.so amdmkl.c

    export LD_PRELOAD=libamdmkl.so

__Permanent fix__

Rather than remembering to set LD_PRLOAD everytime you run your application, add this to your program using:

    patchelf --add-needed libamdmkl.so yourbinary

The information here was taken from [here](https://danieldk.eu/Posts/2020-08-31-MKL-Zen.html).

### Compilers

Recommended compilers will depend on the success seen by your application. See the PDFs below for recommended compiler options on AMD systems. Wisdom about best compilers for particular codes is collected here. Here are the available compilers:

__icc__

`intel_comp/2018` - generally stable

`intel_comp/latest` - possibly better optimisations

`oneAPI` - The newest versions of the Intel compiler, aliased to intel_comp

__gcc__

gnu_comp/ - 10.2 or 11.1 know about the Zen2 architecture, so will be better optimised

__aocc (AMD optimised compiler collection)__

aocc/ - the AMD Optimised Compiler Collection - based on LLVM, use the latest version

__llvm__

Available via the llvm modules

__pgi__

Available via the pgi modules

### MPI Modules

__OpenMPI__

Usually best to use the newest openmpi module. A version of this with .no-ucx (e.g. `openmpi/4.1.1.no-ucx`) may offer more stable performance in some cases.

Large jobs may suffer from performance issues. This can sometimes be resolved by selecting the UD protocol over the newer DC (dynamical connection) protocol by setting:

    export UCX_TLS=self,sm,ud

or

    export UCX_TLS=self,sm,ud,rc,dc

in the job script. See discussion [here](https://github.com/openucx/ucx/issues/4259).

If openmpi is complaining about running out of resources (memory pools being empty), the following may help:

    export UCX_MM_RX_MAX_BUFS=65536
    export UCX_IB_RX_MAX_BUFS=65536
    export UCX_IB_TX_MAX_BUFS=65536

(or some larger value).

UCX settings can be seen with: /cosma/local/ucx/1.10.1/bin/ucx_info -f

For Gadget-4, setting export UCX_UD_MLX5_RX_QUEUE_LEN=16384 has also been shown to help.

__Intel_mpi__

2018 module is the fallback option for SWIFT.

Later versions use UCX underneath, and initially suffered from stability issues. However, the newest versions are much improved.

__Mvapich__

The mvapich module can sometimes offer improved performance. However, in some cases, RAM usage can be increased.

### Tuning information

[Options for compiling on AMD systems](./files/AMDCompileOptions.pdf)

[Tuning for AMD systems](./files/AMDTuning.pdf)

### GPUs

A number of GPU servers are accessible - please ask if you are unsure how to use these:

gn001: 10x NVIDIA V100 GPUs

ga003: 6x AMD MI50 GPUs (now retired)

ga004: 1x AMD MI100 GPU, 2x 64 core AMD Milan processors.

ga005, ga006: 2x AMD MI200 GPUs, 2x 32 core 7513 EPYC processors

login8b, mad04, mad05, mad06: Between 0-3 NVIDIA A100 GPUs (reconfigurable/moveable as required, please ask if you have a particular setup you wish for)

### SWIFT

The current recommended setup (July 2021) is this:

    module load intel_comp/2021.1.0 compiler
    module load intel_mpi/2018
    module load ucx/1.8.1
    module load fftw/3.3.9epyc parallel_hdf5/1.10.6 parmetis/4.0.3-64bit gsl/2.5

You can swap in OpenMPI 4.0.5 instead of intel-mpi and get slightly worse performance.

--bind-to none is required to use all the cores correctly.

The intel_com/2021.1.0 mpi version is also working, if bound correctly to cores.

### Arm Forge

Allinea Arm Forge and MAP (used for code profiling) is available using the allinea/ddt/20.2.1 module.

Profiles collected during the commissioning period are available in the commissioning report.

### SLURM batch scripts

See examples [here](/slurm.md).

### COSMA8 FAQ

The COSMA8 FAQ details some of the known issues or peculiarities related to COSMA8. 

__How do I submit to COSMA8?__

You must be part of a DiRAC project that has an allocation on COSMA8, and be part of the cosma8 group (use the id command to see this). If you are not part of the cosma8 group, but should be, please contact cosma-support. To submit a job script, you need to use -p cosma8.

Jobs failing with `UCX ERROR: ivb_reg_mr`

Try setting the following option in your SLURM batch script (note, this may impact performance):

    export UCX_IB_REG_METHODS=direct

Jobs failing with Bus Error while writing files

This is potentially due to a bug in Lustre 2.12.6. A possible solution is to reduce memory usage. We cannot yet upgrade to newer versions of Lustre, as these have been tested and found to be unstable on COSMA (including 2.12.8 and 2.12.9).

Please let us know if there is something you would like added.

### Known code issues

There is [collective wisdom](/issues.md) available when running particular codes on COSMA8.
