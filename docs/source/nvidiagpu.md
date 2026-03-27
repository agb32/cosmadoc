# NVIDIA GPU testbeds

COSMA contains multiple NVIDIA GPU systems, including H100, A100, V100 and A30 GPUs, to allow code development, porting and performance benchmarking.

There are two Grace-Hopper nodes.

More information is given on the [GPU pages](gpu.md)

## nvhpc

There are nvhpc modules available (`module avail nvhpc`).  It may be necessary to specify a toolchain to use with these, e.g.

```
nvc++ --std=c++20 --gcc-toolchain=/cosma/local/gcc/14.1.0 mycode.cpp
```

On grace-hopper nodes (gn002, gn003), alternative toolchains can be found in `/opt/rh/


The combination of the gcc-15 toolchain with nvc++ 25.1 can cause a compile-time issue with some std:format-related code.  In this case, you can try using gcc-toolset-14, likely nvc++ will complain about a missing gfortran, if this is required.  In this case, make a copy of the gcc-toolset-14 in your apps/ directory, and then copy gfortran/f951 from the gcc-toolet-15 into this.



