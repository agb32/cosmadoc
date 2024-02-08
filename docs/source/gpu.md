# GPUs

COSMA has a number of GPU systems, which are available for use. These are:

* Direct login
  * gn001: 10x NVIDIA V100 GPUs 
  * login8b: 0-3x NVIDIA A100 GPUs (login node)
* cosma8-shm partition
  * mad04: 0-3x NVIDIA A100 GPUs
  * mad05: 0-3x NVIDIA A100 GPUs
  * mad06: 0-3x NVIDIA A100 GPUs
* cosma8-shm2 partition
  * ga004: 1x AMD MI100 GPU
  * ga005: 2x AMD MI200 GPUs
  * ga006: 2x AMD MI200 GPUs
* Retired
  * ga003: 6x AMD MI50 GPUs

We have 3 NVIDIA A100 (40GB) GPUs, which can be moved (in seconds) between login8b, mad04 and mad05, hence the variable number above. If you have a particular requirement, please contact cosma-support. The default configuration is one GPU each in 3 of the nodes. These GPUs are part of a composible PCIe fabric using a [Liqid](https://www.liqid.com) infrastructure funded as part of [ExCALIBUR](https://excalibur.ac.uk).  It is a good idea to add the ```nvidia-smi``` command to your batch script so that you can check that the GPUs are present.

You can use the ```--include``` or ```--exclude``` SLURM parameters within your batch script to specify particular nodes.  Or alternatively, to be given a node with a GPU (within the composable partition), you can use ```--constraint=gpu```.

For nodes not assigned to queues (login8b, gn001), please be aware that these are shared resources and that other people may be using (or may wish to use) them.

