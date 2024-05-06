# The CerIO composable system

The CerIO composable system is a small 8-node cluster.  Each node has 2TB RAM, and access to 8 A30 GPUs, which can be composed to the requested nodes upon demand.

To submit jobs to this cluster, please use the cosma8-cerio Slurm queue.  To determine which project you should select, use the `scontrol show partition=cosma8-cerio` command.  Currently, this includes the durham, do011 (SKA) and do015 projects (use e.g. `#SBATCH -p durham` in your batch submission script).

Further information about how to compose GPUs will appear shortly.
