# Project Data

Access to the data produced by projects using COSMA

## Flamingo

To access data produced by the FLAMINGO project please create a [SAFE](https://safe.epcc.ed.ac.uk/dirac/) account ([instructions](account.md)), and sign up to project do012.

Once access has been granted, you can access COSMA, and submit SLURM jobs to the flamingo partition.

For interactive access you can use e.g.:

srun -p flamingo -A do012 -t 10 --pty /bin/bash

Note that interactive access is not ideal as it will consume compute resource very inefficiently. You are better to submit a [batch script](slurm.md).

If you wish to access the data without a COSMA account, we can make an S3-compatible share available, which will allow you to locally mount the remote file systm - please ask if this would be useful.
