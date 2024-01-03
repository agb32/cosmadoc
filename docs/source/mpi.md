# MPI Hints

This page gathers together various hints for using MPI on COSMA. See also the [Code-specific information](issues.md) page for code-specific hints.

Standard module combinations are:

`intel_comp/2018 and intel_mpi/2018`

`intel_comp/2020-update2` and `intel_mpi/2020-update2` (this uses libfabrics underneath, so may have some bugs not yet ironed out)

Note, when using the newer intel_comp, you first load these, which put some more modules on the search path, allowin you to then "module load compiler mpi" to load the compiler and mpi.

oneAPI/*

`gnu_comp` and `openmpi` (various versions)

## OneAPI / Intel 2021 Compiler

There are modules to run Swift with the Intel 2021.1.0 compiler and Intel MPI or OpenMPI 4.1.1. To use them, load the compiler:

    module load intel_comp/2021.1.0 compiler

Pick Intel MPI or OpenMPI:

    module load mpi 
OR
    module load openmpi/4.1.1

Pick an optimized FFTW:

(Cosma5):
    module load fftw/3.3.9 

OR (Cosma7):

    module load fftw/3.3.9cosma7

OR (Cosma8)

    module load fftw/3.3.9epyc 

and load the other dependencies

    module load parallel_hdf5/1.10.6 parmetis/4.0.3 gsl/2.4

The Intel modules seem to have a bug which prevents them from unloading properly. That's a problem because it means you can't use 'module purge' in scripts to get to a known state.

## mvapich

    module purge
    module load intel_comp/2018 mvapich2 fftw/3.3.7
    module load parallel_hdf5/1.10.3 parmetis/4.0.3
    module load gsl/2.4

Note, the fftw build is optimised for avx512 / cosma7.

