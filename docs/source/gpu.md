# GPUs

COSMA has a number of GPU systems, which are available for use. These are:

* Direct login (from a login node)
  * gn001: 6x NVIDIA V100 GPUs 
  * gn002: NVIDIA Grace-Hopper (ARM) system
  * gn005: NVIDIA RTX PRO 6000 GPU on X86 platform
  * gi001: 2x Intel Ponte Vecchio GPUs (currently dead)
  * mad06: 0-3x NVIDIA A100 GPUs (1TB RAM)
  * ga008: AMD MI300A (4 GPUs, 500GB RAM)
* cosma8-shm Slurm partition (non-DiRAC allocations)
  * mad04: 0-3x NVIDIA A100 GPUs (4TB RAM) - composed on request
  * mad05: 0-3x NVIDIA A100 GPUs (4TB RAM) - composed on request
* cosma8-highram Slurm partition (DiRAC allocations)
  * mad04: 0-3x NVIDIA A100 GPUs (4TB RAM) - composed on request
  * mad05: 0-3x NVIDIA A100 GPUs (4TB RAM) - composed on request
* cosma8-draper Slurm partition (DiRAC allocations for MI300X system)
  * ga007: 8x AMD MI300 GPUs
* cosma8-dine2 Slurm partition (DiRAC allocations for the cosma8-dine2 cluster with A30 GPUs - composable)
  * gc[001-008]: 0-8x NVIDIA A30 GPUs, 0-4x NVIDIA V100 GPUs
* cosma8-shm2 Slurm partition
  * ga004: 1x AMD MI100 GPU
  * ga005: 2x AMD MI210 GPUs
  * ga006: 2x AMD MI210 GPUs
* dine2 Slurm partition
  * gc[001-008]: 0-8x NVIDIA A30 GPUs, 0-4x NVIDIA V100 GPUs
* gracehopper Slurm partition
  * gn003: NVIDIA Grace-Hopper (ARM) system
* intelhopper Slurm partition
  * gn004: NVIDIA H100 GPU on X86 platform
* mi300x, mi300x-prince partition: AMD MI300X system
  * ga007: 8x AMD MI300 GPUs
* Retired
  * ga003: 6x AMD MI50 GPUs

## Project codes

To use the GPUs which are in a Slurm partition, you must either be part of a DiRAC project with a current allocation on the system, or sign up to the following project codes in [SAFE](https://safe.epcc.ed.ac.uk/dirac) as part of the hardware lab:

- do015: dine2 partition
- do016: NVIDIA Grace Hopper GPUs, H100, cosma8-shm partition
- do017: Intel GPUs (currently dead)
- do018: AMD GPUs

DiRAC allocated projects will have higher priority.

To use a GPU available for direct login, just ssh to the node name given above.

**Note:** Some GPU nodes are in a hybrid mode to allow for testing during office hours and production workloads during the night.  Further information is available in the motd of relevant nodes.

## GPU stats

| GPU | FP64 TFLOPS | RAM/GB | Memory bandwidth/GB/s |
| --- | ----------- | --- | ---------------- |
| V100 | 7 | 32 | 900 |
| A100 |9.7 | 40 | 1555 |
| A30 | 5.2 | 24 | 933 |
| H100 PCIe | 26 | 80 | 2000 |
| H100 SMX | 34 | 80 | 3350 |
| RTX PRO 6000  | 2 (126 for FP32) | 96 | 1790
| MI50 | 6.6 | 16 | 1000 |
| MI100 | 11.5 | 32 | 1200 |
| MI210 | 22.6 | 64 | 1600 |
| MI300X | 81.7 | 192 | 5300 |
| MI300A | 61.3 | 128 | 5300 |
| PVC | 52.4 | 128 | 3280 |

For detailed notes on GPU specifications and usage, see the following pages:

## [AMD GPUs](amdgpu.md)

## [NVIDIA GPUs](nvidiagpu.md)

## Further notes on GPUs

For nodes not assigned to queues (mad06, gn001, gn002, gn005, ga008, gi001), please be aware that these are shared resources and that other people may be using (or may wish to use) them.

To use some of these GPUs, you may need to be in the "video" or "render" groups (use the ```id``` command to check which groups you are in).  If you are not in it, but need to be, please ask.

To check that you have the correct permissions to submit to a partition, you can use the ```scontrol show partition=PARTITION_NAME``` command to see which groups are allow to submit to that partition.

The Intel PVC GPUs on gi001 are currently dead - sometime in Autumn 2025.  Watch this space - we may be able to resurrect them.

