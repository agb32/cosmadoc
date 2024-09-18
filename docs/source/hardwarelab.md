# Hardware lab

The COSMA hardware laboratory is used for prototyping and development of new systems and technologies.  Many of the systems tested are readily available for benchmarking.

## DINE and DINE2

DINE and DINE2 are experimental test clusters for exploring new hardware and networking technologies.

The [BlueField DPU cluster](bluefield.md), [DINE](dine.md), is equipped with 24 nodes each containing a NVIDIA BlueField-2 Data Processing Unit, with HDR200 InfiniBand connectivity.  To use this facility submit jobs to the bluefield1 Slurm partition.  It was previously equipped with BlueField1 and Rockport network cards.

The [DINE2](dine.md) cluster is an 8 node cluster equipped with a CerIO composability fabric, allowing GPUs to be added to servers upon demand.

## GPU compute

We maintain multiple generations of GPU architecture from multiple vendors.

### AMD GPU nodes

There are [two nodes](amdgpu.md) each with two AMD MI200 GPUs available.  Submit jobs to the cosma8-shm2 partition.  This partition also contains a node with one AMD MI100 GPU.  To specify a particular GPU to submit to, use --exclude or --include.

### NVIDIA GPU nodes

V100, A100 and H100 nodes are [available for use](nvidiagpu.md).

### Intel GPU nodes

A Ponte Vecchio GPU node is [available](intelgpu.md)

## Composable infrastructure

COSMA contains a [composable](composable.md) GPU and RAM system, attached to login8b and the cosma8-shm queue.  If you need to use these resources in a different configuration, please ask cosma-support.

It also contains an 8-node system with 8 A30 GPUs, allowing up to 8 GPUs per node, based on a CerIO composable fabric.

## Rockport network fabric

The [Rockport network fabric](rockport.md) is 6D torus network with 100G connectivity, installed as half of COSMA7.  To use this, please submit to the cosma7-rp Slurm partition.

## DWAVE quantum

The ExCALIBUR project funds [quantum annealing system access](quantum.md) via a DWAVE system, which is administered by COSMA staff.  Please contact cosma-support if you need access. 

## CPU compute lab

A wide variety of [processor technologies](cpucomputelab.md) are available for testing and benchmarking and we try to maintain cutting-edge components.

## Storage

Our [storage laboratory](storagelab.md) includes prototype and production file systems of various types and technologies.

## Solar

Our [solar installation](environmental.md#solar-panels) provides power directly usable by COSMA, allowing us to study the interplay between solar energy generation and HPC power usage.

## Immersion cooling

We have funds to install a prototype [immersion cooling](immersion.md) tank, and provide access to this facility to HPC technical support teams from across the UK, to help reduce the entry barrier to this technology.
