# Composability

COSMA has two composable systems to allow experimentation with composability, i.e. the ability to define server components within software.

## Liqid system

A Liqid system installed in 2021 has 3 nodes (including a direct access node) to which both GPU and RAM can be composed upon demand (i.e. a request to cosma-support).

The GPUs are NVIDIA A100-40GB.  There are 3 GPUs which can be configured between the nodes.  To select a node containing a GPU, please add `#SBATCH --constraint=gpu` to your batch script.  See the [GPU page](gpu.md) for more details.  Typically, we compose one GPU per node.

The composed RAM is also usually shared between the nodes and presented as swap space.

The default configuration has one GPU per node.  Queues hosting these nodes include cosma8-shm2, cosma8-ska2, cosma8-highram.  The direct ssh node is mad06.

## CerIO system

A [CerIO](cerio.md) system installed in 2024 has 8 nodes which share 12 GPUs (8x A30, 4x V100), allowing servers with up to 8 GPUs to be configured.  Follow the [instructions](cerio.md) to use this system.
