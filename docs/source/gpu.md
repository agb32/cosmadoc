# GPUs

COSMA has a number of GPU systems, which are available for use. These are:

* gn001: 10x NVIDIA V100 GPUs
* ga003: 6x AMD MI50 GPUs
* ga004: 1x AMD MI100 GPU
* login8b: 0-3x NVIDIA A100 GPUs
* mad04: 0-3x NVIDIA A100 GPUs
* mad05: 0-3x NVIDIA A100 GPUs
* ga005: 2x AMD MI200 GPUs
* ga006: 2x AMD MI200 GPUs

We have 3 NVIDIA A100 (40GB) GPUs, which can be moved (in seconds) between login8b, mad04 and mad05, hence the variable number above. If you have a particular requirement, please contact cosma-support. The default configuration is one GPU per node. These GPUs are part of a composible PCIe fabric using a [Liqid](https://www.liqid.com) infrastructure funded as part of [ExCALIBUR](https://excalibur.ac.uk).

To use mad04 and mad05, please submit to the cosma8-shm queue. To use the others, please ssh directly to them, from a login node, and be aware that they are a shared resource (i.e. other people might be using them).