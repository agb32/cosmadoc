# CPU Compute Lab

The CPU Compute Lab provides access to latest generation CPU technologies, to enable code porting and optimisation by UK researchers in preparation for future large production systems.

Current systems include
- [Sapphire Rapids (2024)](#more-on-sapphire-rapids)
  - Direct ssh to the gi001 node
  - Via the dine2 Slurm partition
- Bergamo (2023)
  - Via the cosma5 Slurm partition
- Genoa (2023)
  - Via the cosma8-shm3 Slurm partition
- IceLake (2022)
  - Via the cosma8-ska Slurm partition
- Milan (2021)
  - Via the cosma8-milan Slurm partition
- Rome (2019)
  - Via the cosma8-rome Slurm partition
- CascadeLake (2019)
  - Via the cosma7-shm2 Slurm partition

## More on Sapphire Rapids

### Node access

Our Sapphire Rapids are configured to hold Ponte Vecchio GPUs (PVCs). Therefore, they are accessible as part of our Intel GPU nodes.

(*) The nodes are given out FCFS, i.e. please check prior to any benchmarking that nobody else is currently using the node.

### Specification

- CPU name:       Intel(R) Xeon(R) Platinum 8480+
- Sockets:                2
- Cores per socket:       56
- Threads per core:       2

### Environment

As this is an Intel node while Cosma's login nodes are AMD, we recommend to compile exclusively on the node:

```sh
module load intel_comp
module load compiler-rt tbb compiler mpi
```

The module oneAPI should work as well.

### Performance

To assess the node's performance, we recommend to run

```sh
module load likwid
likwid-bench
```

Type in -a or -h to see an overview of the available metrics. Stream Triad and peak are the ones we usually recommend to look at first.

