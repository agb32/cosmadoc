# HPC Hardware Lab @Durham

The [HPC Hardware Laboratory @Durham](https://durham.readthedocs.io/en/latest/hardwarelab) is used for prototyping and development of new systems and technologies.  Many of the systems tested are readily available for benchmarking.  Details of available nodes and GPUs can be found [here](hardwarelabsummary.md).

To request access to any of the systems within the hardware lab, please [create an account](account.md) and request to join the corresponding [project code](gpu.md#project-codes).

The Hardware Lab features the following systems and technologies:  
[DINE and DINE2](#dine-and-dine2)  
[GPU compute nodes](#gpu-compute)  
[Composable Infrastructure](#composable-infrastructure)  
[Rockport Network Fabric](#rockport-network-fabric)  
[Quantum Annealing (DWAVE)](#dwave-quantum)  
[CPU Compute Lab](#cpu-compute-lab)  
[Storage Lab](#storage-lab)  
[Solar Power](#solar)  
[Immersion Cooling](#immersion-cooling)  
[Heat Storage](#heat-storage)  



## DINE and DINE2

DINE and DINE2 are experimental test clusters for exploring new hardware and networking technologies.

![DINE](images/dine.png)

The [BlueField DPU cluster](bluefield.md), [DINE](dine.md), is equipped with 24 nodes, each containing a NVIDIA BlueField-2 Data Processing Unit, with HDR200 InfiniBand connectivity.  To use this facility, submit jobs to the bluefield1 Slurm partition.  It was previously equipped with BlueField1 and Rockport network cards.

The [DINE2](dine.md) cluster is an 8-node cluster equipped with a CerIO composability fabric, allowing GPUs to be added to servers upon demand.  To use the DINE2 cluster as a Hardware Lab user, apply to join the do015 project.

## GPU compute

We maintain [multiple generations of GPU architecture](gpu.md) from multiple vendors.

### AMD GPU nodes

We have multiple generations of AMD MI GPU:
- MI100
- MI210
- MI300A
- MI300X

There are [two nodes](amdgpu.md), each with two AMD MI200 GPUs available.  Submit jobs to the cosma8-shm2 partition.  This partition also contains a node with one AMD MI100 GPU.  To specify a particular GPU to submit to, use --exclude or --include.

For the MI300 GPUs, either submit to the mi300x queue, or ssh directly from a login node to the ga008 node (MI300X).

### NVIDIA GPU nodes

V100, A100 and H100 nodes are [available for use](nvidiagpu.md), including Intel-Hopper (X86 CPU) and Grace-Hopper (ARM CPU).

### Intel GPU nodes

A [Ponte Vecchio GPU](intelgpu.md) node was once available but is currently offline.

### Tenstorrent Blackhole node (RISC-V)

A [Tenstorrent Blackhole](tenstorrent.md) server is available for interactive use, containing 4x Blackhole cards.  

Tenstorrent cards are designed specifically for AI and machine-learning workloads, unlike GPUs which have been adapted over time from their original graphics rendering workloads.  Currently PyTorch, ONNX, and TensorFlow can be easily ported to Tenstorrent architecture, but software support is otherwise in the early stages of development.

## Composable infrastructure

COSMA contains a [composable](composable.md) GPU and RAM system, attached to the cosma8-shm queue.  If you need to use these resources in a different configuration, please ask cosma-support.

COSMA also hosts an 8-node system with 8x A30 GPUs, allowing up to 8 GPUs per node, based on a CerIO composable fabric.

## Rockport network fabric

The [Rockport network fabric](rockport.md) is 6D torus network with 100G connectivity, installed as half of COSMA7.  To use this, please submit to the cosma7-rp Slurm partition.

## DWAVE quantum

The ExCALIBUR project funded [quantum annealing system access](quantum.md) via a DWAVE system, which was administered by COSMA staff.  This has now expired, but if you are interested in access, please contact cosma-support.

## CPU compute lab

A wide variety of [processor technologies](cpucomputelab.md) are available for testing and benchmarking and we try to maintain cutting-edge components.

## Storage lab

Our [storage laboratory](storagelab.md) includes prototype and production file systems of various types and technologies.

## Solar

Our [solar installation](environmental.md#solar-panels) provides power directly usable by COSMA, allowing us to study the interplay between solar energy generation and HPC power usage.

## Immersion cooling

We have a prototype [immersion cooling](immersion.md) tank, and provide access to this facility to HPC technical support teams from across the UK, to help reduce the entry barrier to this technology, and to develop experience using it.

## Heat storage

We are investigating the [inter-seasonal storage of waste data centre heat](https://durham.readthedocs.io/en/latest/ichs/index.html) using abandoned flooded coal mines beneath the data centre site, to allow this heat to be used for building heating during the colder winter months.




