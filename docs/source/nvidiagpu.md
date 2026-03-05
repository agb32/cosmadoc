# NVIDIA GPU testbeds

COSMA contains multiple NVIDIA GPU systems, including V100, A100 and A30 GPUs, to allow code development, porting and performance benchmarking.

There are also two Grace Hopper nodes.

More information is given on the [GPU pages](gpu.md)

## nvhpc

There are nvhpc modules available (`module avail nvhpc`).  It may be necessary to specify a toolchain to use with these, e.g.

```
nvc++ --std=c++20 --gcc-toolchain=/cosma/local/gcc/14.1.0 mycode.cpp
```

On grace-hopper nodes (gn002, gn003), alternative toolchains can be found in `/opt/rh/
