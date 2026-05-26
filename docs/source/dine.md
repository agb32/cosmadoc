# DINE

The Durham Interconnected Novel Environment (DINE) is a test production cluster aimed at testing different HPC, networking and storage technologies.  It is now in the second generation.

To date, it has hosted BlueField-1, Rockport and BlueField-2 technologies.

Installed in 2019, DINE was the first UK AMD Rome based production cluster.

## Specifications

The DINE cluster consists of 24 nodes, each equipped with a 200G BlueField-2 Data Processing Unit from NVIDIA.
DPUs offload networking and storage workloads from the main CPU of the node, separating infrastructure processing from job processing.

| Nodes | RAM per node | CPU(s) | Network Technology |
| --- | --- | --- | --- |
| 24 | 512GB | 2x AMD EPYC 7302 16-Core | Infiniband |


## Usage

If you do not already have an account on COSMA, please follow the instructions [here](account.md), then request to join the project: do009.

The DINE cluster is part of the `bluefield1` SLURM partition.  Jobs should be submitted to the queue using `#SBATCH -p bluefield1`.

There is no direct ssh access to DINE nodes.

## Known issues / notes

The bluefield nodes are automatically powered down when not in use, so when you submit your job you may see the status as `CF` (configuring) while your allocated nodes are booting.
