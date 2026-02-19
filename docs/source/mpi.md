# MPI Hints

This page gathers together various hints for using MPI on COSMA. See also the [Code-specific information](issues.md) page for code-specific hints.

Standard module combinations are:

`intel_comp/2018 and intel_mpi/2018`

`intel_comp/2025.3.0` (or other latest version) and then (following the instructions printed out) `compiler-rt tbb umf compiler mpi`. 

Note, when using the newer intel_comp modules, you first load these, which put some more modules on the search path, allowing you to then "module load compiler mpi" to load the compiler and mpi (compiler-rt and tbb may also be needed, depending on version). 

`oneAPI/* ` (which is an alias for intel_comp)

`gnu_comp` and `openmpi` (various versions)

## OneAPI / Intel 2024 Compiler

There are modules to run Swift with the Intel 2024.2.0 compiler and Intel MPI or OpenMPI 5.0.3. To use them, load the compiler:

```
module load intel_comp/2024.2.0 compiler-rt tbb compiler
```

Pick Intel MPI or OpenMPI:

```
module load mpi
```

OR

```
module load openmpi/5.0.3
```

Pick an optimized FFTW:

- (Cosma5):    `module load fftw/3.3.10 `

- OR (Cosma7):   `module load fftw/3.3.10cosma7`

- OR (Cosma8): `module load fftw/3.3.10cosma8`

and load the other dependencies

```module load parallel_hdf5 parmetis gsl```

(note, there may be specific version of these that improve performance, check using the `module avail` command)

The Intel modules seem to have a bug which prevents them from unloading properly. That's a problem because it means you can't use 'module purge' in scripts to get to a known state.

## mvapich

This is not regularly tested.

```
    module purge
    module load intel_comp/2018 mvapich2 fftw/3.3.7
    module load parallel_hdf5/1.10.3 parmetis/4.0.3
    module load gsl/2.4
```

Note, the fftw build is optimised for avx512 / cosma7.

# Compiling openMPI with ROCm

Some success has been achieved using the following instructions on a node with ROCm installed (one of the AMD GPU nodes):

- Compiling UCX

`../configure --prefix=/cosma/apps/PROJECT/USER/ucx-1.19.0 --with-rocm=/opt/rocm --without-knem --without-cuda --enable-mt`

- Compiling UCC

`../configure --prefix=/cosma/apps/PROJECT/USER/ucc-1.6.0 --with-rocm=/opt/rocm --with-ucx=/cosma/apps/PROJECT/USER/ucx-1.19.0`

- Compiling OpenMPI

`../configure --prefix=/cosma/apps/PROJECT/USER/openmpi-5.0.9 --with-rocm=/opt/rocm --with-ucx=/cosma/apps/PROJECT/USER/ucx-1.19.0 --with-ucc=/cosma/apps/PROJECT/USER/ucc-1.6.0 --without-cuda`

