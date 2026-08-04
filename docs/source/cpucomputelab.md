# CPU Compute Lab

The CPU Compute Lab provides access to latest generation CPU technologies, to enable code porting and optimisation by UK researchers in preparation for future large production systems.

Current systems include
- Intel Sierra Forest
  - Direct ssh to the mad11 node
- AMD Turin
   - Direct ssh to the mad12 node
- [Intel Sapphire Rapids (2024)](#more-on-sapphire-rapids)
  - Direct ssh to the gi001 node
  - Via the dine2 Slurm partition (apply to join do015)
- AMD Bergamo (2023)
  - Via the cosma5 Slurm partition (apply to join hpcicc)
- AMD Genoa (2023)
  - Via the cosma8-shm3 Slurm partition (apply to join do009)
- Intel IceLake (2022)
  - Via the cosma8-ska Slurm partition (apply to join do011)
- AMD Milan (2021)
  - Via the cosma8-milan Slurm partition
- AMD Milan-X (2022, high L3 cache variant)
  - Direct ssh to the mad06 node
- AMD Rome (2019)
  - Via the cosma8-rome Slurm partition
- Intel CascadeLake (2019)
  - Via the cosma7-shm2 Slurm partition

## More on Sapphire Rapids

We have two systems with Intel Sapphire Rapids CPUs.
- A single node, gi001, also containing Ponte Vecchio GPUs
  - CPU name:       Intel(R) Xeon(R) Platinum 8480+
  - Sockets:                2
  - Cores per socket:       56
  - Threads per core:       2
  - RAM:	      		  512 GB
  - Network: HDR200 InfiniBand
- The DINE2 system with 8 nodes
  - CPU model: Intel(R) Xeon(R) Gold 6430
  - Sockets: 2
  - Cores per socket: 32
  - Threads per core: 2
  - RAM: 2TB
  - Network: HDR200 InfiniBand
  
### Node access

Our single node Sapphire Rapids system contins Ponte Vecchio GPUs (PVCs). Therefore, they are accessible as part of our Intel GPU nodes.

(*) The nodes are given out FCFS, i.e. please check prior to any benchmarking that nobody else is currently using the node.

The DINE2 system can be accessed via the dine2 Slurm partition.

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

