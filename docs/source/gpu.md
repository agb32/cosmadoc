# GPUs

COSMA has a number of GPU systems, which are available for use. These are:

* Direct login
  * gn001: 10x NVIDIA V100 GPUs 
  * login8b: 0-3x NVIDIA A100 GPUs (login node)
  * gn002: NVIDIA Grace-Hopper (ARM) system
  * gi003: 2x Intel Ponte Vecchio GPUs
* cosma8-shm Slurm partition
  * mad04: 0-3x NVIDIA A100 GPUs
  * mad05: 0-3x NVIDIA A100 GPUs
  * mad06: 0-3x NVIDIA A100 GPUs
* cosma8-shm2 Slurm partition
  * ga004: 1x AMD MI100 GPU
  * ga005: 2x AMD MI200 GPUs
  * ga006: 2x AMD MI200 GPUs
* dine2 Slurm partition
  * gc[001-008]: 0-8x NVIDIA A30 GPUs
* gracehopper Slurm partition
  * gn003: NVIDIA Grace-Hopper (ARM) system
* Retired
  * ga003: 6x AMD MI50 GPUs

## Project codes

To use the GPUs, please sign up to the following project codes in SAFE:

- do015: dine2 partition
- do016: NVIDIA Grace Hopper GPUs, cosma8-shm partition
- do017: Intel GPUs
- do018: AMD GPUs
- 

## Using the composable A100 GPUs

We have 3 NVIDIA A100 (40GB) GPUs, which can be moved (by software, in seconds, in theory!) between login8b, mad04, mad05 and mad06, hence the variable number above. If you have a particular requirement, please contact cosma-support. The default configuration is one GPU each in 2 of the 3 nodes (mad04,05,06) and one on the login node (login8b). These GPUs are part of a composible PCIe fabric using a [Liqid](https://www.liqid.com) infrastructure funded as part of [ExCALIBUR](https://excalibur.ac.uk).  It is a good idea to add the ```nvidia-smi``` command to your batch script so that you can check that the GPUs are present.

You can use the ```--include``` or ```--exclude``` SLURM parameters within your batch script to specify particular nodes.  Or alternatively, to be given a node with a GPU (within the composable partition), you can use ```#SBATCH --constraint=gpu```.

## GPU notes

For nodes not assigned to queues (login8b, gn001), please be aware that these are shared resources and that other people may be using (or may wish to use) them.

To use some of these GPUs, you will need to be in the "video" group (use the ```id``` command to check which groups you are in).  If you are not in it, but need to be, please ask.

To check that you have the correct permissions to submit to a partition, you can use the ```scontrol show partition=PARTITION_NAME``` command to see which groups are allow to submit to that partition.

## DINE2

The DINE2 GPU system is a composable system with up to 8 A30 GPUs per node.  Currently these are static (i.e. if you require a specific GPU configuration, please ask), but eventually we hope to make it dynamic (i.e. to be able to ask Slurm to compose a system).  In total, there are 8 GPUs, and these can be composed in any configuration to the 8 servers.

Each server has dual 32-core Sapphire Rapids CPUs and 2TB RAM.

To use these nodes, submit jobs to the dine2 partition.

## Grace-Hopper

The Grace-Hopper nodes are currently available for direct ssh from a login node (gn002, gn003).  Eventually, one will be made into a Slurm queue.

## Ponte Vecchio

The Intel Ponte Vecchio node (donated by Intel) is available for direct ssh from a login node (gi001).

