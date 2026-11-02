# GPU jobs

How you request a GPU depends on the queue, so a job script for one queue may not work on another.  See [GPUs](gpu.md) for the hardware, and for the [project codes](gpu.md#project-codes) that give you access.

## Requesting a GPU

| Queue | Nodes | GPUs | How to request one |
| ----- | ----- | ---- | ------------------ |
| `cosma8-shm` | mad04, mad05 | NVIDIA A100 | `--gres=gpu:1` |
| `cosma8-shm2` | ga004, ga006 | AMD MI100, MI210 | `--gres=gpu:1` |
| `gracehopper` | gn003 | NVIDIA GH200 | `--gres=gpu:1` |
| `dine2` | gc001-gc008 | NVIDIA A30, V100 | `--constraint=gpu` |
| `mi300x`, `cosma8-draper` | ga007 | AMD MI300X | `--gpus=N` |

The GPUs on `dine2` are composable, and are not tracked by Slurm, so `--gres=gpu:1` is rejected with `Requested node configuration is not available`.  `--constraint=gpu` selects a node with GPUs attached.  At the time of writing, these are gc004 and gc008.

The hybrid nodes, including gn004 and gn005, are available in the `hardwarelab-gpu` queue overnight: see [hybrid nodes](hardwarelab-hybridnodes.md).

## Example job script

This example runs on an NVIDIA A100 on `cosma8-shm`:

```
#!/bin/bash -l
#SBATCH -J gpujob
#SBATCH -o gpujob.%j.out
#SBATCH -p cosma8-shm
#SBATCH -A PROJECT
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH -t 01:00:00

module purge
module load nvhpc

echo "Using GPU $CUDA_VISIBLE_DEVICES on $(hostname)"
nvidia-smi
./myprogram
```

For `dine2`, replace `-p cosma8-shm` with `-p dine2`, and `--gres=gpu:1` with `--constraint=gpu`.  For an AMD GPU on `cosma8-shm2`, change the queue, and use `rocm-smi` or your own program instead of `nvidia-smi`.

## Check that your job has a GPU

When you use `--gres`, Slurm sets `CUDA_VISIBLE_DEVICES` and `ROCR_VISIBLE_DEVICES` to show which GPUs your job should use.

Requesting a GPU this way matters even when a GPU is visible without it.  A job on `cosma8-shm` without `--gres` can still see the node's GPU, but Slurm has not reserved it, so another job may be using it.

With `--constraint=gpu` on `dine2`, `CUDA_VISIBLE_DEVICES` is not set, and your job can see all of the node's GPUs.  Other jobs on the node may be using them, so use `nvidia-smi` to check.

## Choosing a node

To select a particular type of GPU on a queue with a mix of nodes, use `--nodelist` or `--exclude`:

```
#SBATCH -p cosma8-shm2
#SBATCH --gres=gpu:1
#SBATCH --nodelist=ga006
```

If you need more GPUs on a composable node, please contact cosma-support: see [composable systems](composable.md).

## Interactive use

To get a shell on a GPU node:

```
srun -p cosma8-shm -A PROJECT --gres=gpu:1 -c 8 --mem=32G -t 01:00:00 --pty /bin/bash
```

Some GPU nodes can also be reached directly with `ssh` from a login node: see [GPUs](gpu.md).
