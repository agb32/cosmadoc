# DINE2

DINE2, the Durham Investigatory Node Environment (or Durham Integrated Next-gen Environment), is an 8 node cluster with a CerIO composability fabric, allowing GPUs to be added to servers upon demand.

With dual Intel Sapphire Rapids 32-core processors and 2TB RAM.  Each node has access to up to 8 NVIDIA A30 GPUs, using a CerIO composable fabric.

DINE2 was installed in 2024.

## Specifications

| Nodes | RAM per node | CPU(s) | Network Technology | GPU | GPU Count |
| --- | --- | --- | --- | --- | --- |
| 8 | 2TB | 2x Intel Sapphire Rapids 32-core | Infiniband | Nvidia A30 24GB | 8 Total (configurable) |

By default, each node has a single GPU attached, but can be configured to use up to the 8 available.  
To request a specific configuration, please contact `cosma-support@durham.ac.uk`.

### Benchmarks

- Memory bandwidth (BabelStream): 822 GB/s
- array\_size: 134217728
- iterations: 100
- precision: FP64

Futher details are available on the [SHAREing website](https://shareing-dri.github.io/hpc-testbeds/systems/cosma-a30/).

## Usage

If you do not already have an account on COSMA, please follow the instructions [here](account.md), then request to join the project: do015.

The DINE2 cluster is part of the `dine2` SLURM partition.  Jobs should be submitted to the queue using `#SBATCH -p dine2`.

There is no direct ssh access to DINE nodes.

CUDA is available as a module, using `module load nvhpc/25.11`.

## Known issues / notes

Dine2 nodes mount /dine, not /cosma5.  Copy any necessary files into /dine/data/\<project\>/\<username\>/

