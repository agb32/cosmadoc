# GPUs

COSMA has a number of GPU systems, which are available for use. These are:

* Direct login (from a login node)
  * gn001: 10x NVIDIA V100 GPUs 
  * gn002: NVIDIA Grace-Hopper (ARM) system
  * gn004: NVIDIA H100 GPU on X86 platform
  * gi001: 2x Intel Ponte Vecchio GPUs (currently dead)
  * mad06: 0-3x NVIDIA A100 GPUs (1TB RAM)
  * ga008: AMD MI300A (4 GPUs, 500GB RAM)
* cosma8-shm Slurm partition
  * mad04: 0-3x NVIDIA A100 GPUs (4TB RAM)
  * mad05: 0-3x NVIDIA A100 GPUs (4TB RAM)
* cosma8-shm2 Slurm partition
  * ga004: 1x AMD MI100 GPU
  * ga005: 2x AMD MI210 GPUs
  * ga006: 2x AMD MI210 GPUs
* dine2 Slurm partition
  * gc[001-008]: 0-8x NVIDIA A30 GPUs
* gracehopper Slurm partition
  * gn003: NVIDIA Grace-Hopper (ARM) system
* mi300x, mi300x-prince partition: AMD MI300X system
  * ga007: 8x AMD MI300 GPUs
* Retired
  * ga003: 6x AMD MI50 GPUs

## Project codes

To use the GPUs, please sign up to the following project codes in SAFE:

- do015: dine2 partition
- do016: NVIDIA Grace Hopper GPUs, H100, cosma8-shm partition
- do017: Intel GPUs (currently dead)
- do018: AMD GPUs
 
## GPU stats

| GPU | FP64 TFLOPS | RAM/GB | Memory bandwidth/GB/s |
| --- | ----------- | --- | ---------------- |
| V100 | 7 | 32 | 900 |
| A100 |9.7 | 40 | 1555 |
| A30 | 5.2 | 24 | 933 |
| H100 PCIe | 26 | 80 | 2000 |
| H100 SMX | 34 | 80 | 3350 |
| MI50 | 6.6 | 16 | 1000 |
| MI100 | 11.5 | 32 | 1200 |
| MI210 | 22.6 | 64 | 1600 |
| MI300X | 81.7 | 192 | 5300 |
| MI300A | 61.3 | 128 | 5300 |
| PVC | 52.4 | 128 | 3280 |


## Using the composable A100 GPUs

We have 3 NVIDIA A100 (40GB) GPUs, which can be moved (by software, in seconds, in theory!) between mad04, mad05 and mad06, hence the variable number above. If you have a particular requirement, please contact cosma-support. The default configuration is one GPU each (mad04,05,06). These GPUs are part of a composable PCIe fabric using a [Liqid](https://www.liqid.com) infrastructure funded as part of [ExCALIBUR](https://excalibur.ac.uk).  It is a good idea to add the ```nvidia-smi``` command to your batch script so that you can check that the GPUs are present.

You can use the ```--include``` or ```--exclude``` SLURM parameters within your batch script to specify particular nodes.  Or alternatively, to be given a node with a GPU (within the composable partition), you can use ```#SBATCH --constraint=gpu```.

## GPU notes

For nodes not assigned to queues (mad06, gn001, gn002, gi001), please be aware that these are shared resources and that other people may be using (or may wish to use) them.

To use some of these GPUs, you may need to be in the "video" or "render" groups (use the ```id``` command to check which groups you are in).  If you are not in it, but need to be, please ask.

To check that you have the correct permissions to submit to a partition, you can use the ```scontrol show partition=PARTITION_NAME``` command to see which groups are allow to submit to that partition.

The Intel PVC GPUs on gi001 are currently dead - sometime in Autumn 2025.  Watch this space - we may be able to resurrect them.

## DINE2

The DINE2 GPU system is a composable system with up to 8 A30 GPUs per node.  Currently these are static (i.e. if you require a specific GPU configuration, please ask), but eventually we hope to make it dynamic (i.e. to be able to ask Slurm to compose a system).  In total, there are 8 GPUs, and these can be composed in any configuration to the 8 servers.

Each server has dual 32-core Sapphire Rapids CPUs (64 cores per node) and 2TB RAM.

To use these nodes, submit jobs to the dine2 partition.

## Grace-Hopper

One Grace-Hopper node is currently available for direct ssh from a login node (gn002).  ga003 is available in a Slurm queue, gracehopper.

Note, the Grace CPU has an ARM architecture, and therefore X86 binaries will not run.  The NVIDIA and GCC compilers are available.

## Ponte Vecchio

This node is currently dead.

The Intel Ponte Vecchio node (donated by Intel) is available for direct ssh from a login node (gi001).

OneAPI is available using the intel_comp modules, e.g. `module load intel_comp` (or `module load oneAPI`).

## MI300X

The MI300X node has 8x GPUs, and is available in the mi300x slurm partition.

The AMD ROCm software stack is installed.

Any codes currently using CUDA will need to be HIP-ified by running the hipify script provided as part of ROCm.  Fine tuning may be necessary to optimise performance.

To get interactive access you could use `srun -p mi300x -A do018 -t 10 --pty /bin/bash`, and if you want exclusive access to the GPUs (e.g. for benchmarking), use the `--exclusive` flag.

There was a DiRAC hackathon in April 2025 focused on AMD GPUs, which was very relevant to any users of this system.  There will be future hackathons - watch out for them!

## MI300A

The MI300A system has 4x GPUs, and is available for direct ssh (to ga008) from a login node.

The AMD ROCm software stack is installed.

Any codes currently using CUDA will need to be HIP-ified by running the hipify script provided as part of ROCm.  Fine tuning may be necessary to optimise performance.

The MI300A is an APU: The GPU and CPU are part of the same silicon, and share the same physical RAM.  Therefore, memory copies between CPU and GPU are not necessary, which can significantly improve performance for many applications, and make it highly appropriate for some codes which cannot easily be ported to more traditional GPU architectures.

## H100

There is a single PCIe-based NVIDIA H100 GPU with an X86 (Intel) host, which is available for direct ssh.
