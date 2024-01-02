# Hardware lab

The COSMA hardware laboratory is used for prototyping and development of new systems and technologies.  Many of the systems tested are readily available for benchmarking.

## BlueField DPU cluster

The BlueField DPU cluster, DINE, is equipped with 24 nodes each containing a NVIDIA BlueField-2 Data Processing Unit, with HDR200 InfiniBand connectivity.  To use this facility submit jobs to the bluefield1 Slurm partition.

## AMD GPU nodes

There are two nodes each with two AMD MI200 GPUs available.  Submit jobs to the cosma8-shm2 partition.  This partition also contains a node with one AMD MI100 GPU.  To specify a particular GPU to submit to, use --exclude or --include.

## Composable infrastructure

COSMA contains a composable GPU and RAM system, attached to login8b and the cosma8-shm queue.  If you need to use these resources in a different configuration, please ask cosma-support.

## Rockport network fabric

The Rockport network fabric is 6D torus network with 100G connectivity, installed as half of COSMA7.  To use this, please submit to the cosma7-rp Slurm partition.

## DWAVE quantum

The ExCALIBUR project funds quantum annealing system access via a DWAVE system, which is administered by COSMA staff.  Please contact cosma-support if you need access.