# COSMA job queues

COSMA8 queues: cosma8, cosma8-prince, cosma8-pauper, cosma8-serial, cosma8-shm, cosma8-shm2

Access to the DiRAC COSMA8 system is only for DiRAC projects with a time allocation on this system. Each COSMA8 compute node has 128 cores and 1TB RAM. If you request fewer than 128 cores for a job using the cosma8-serial queue, you will not be granted exclusive access to a node, and therefore may share a node with other jobs. Unless you specify a memory in your SLURM script (e.g. ```bash #SBATCH --mem=1T```), then you will be given a fraction of 1TB equal to the number of cores you request/128. If you do not wish to share a node, use the "#SBATCH --exclusive" flag. The cosma8-shm queue provides access to two large 4TB nodes, each with 128 cores.

The cosma8-prince queue requires special access permission, will give an elevated priority and allow jobs to run for 30 days.

The cosma8-pauper queue is a low priority queue with a limit of 1 day runtime, automatically used by projects that have exceeded their time allocation.

## cosma8-shm, cosma8-shm2

The cosma8-shm and cosma8-shm2 queues are small queues with non-standard hardware.

cosma8-shm contains:

* mad04: 128 cores, 4TB RAM, 0-3 NVIDIA A100 GPUs
* mad05: 128 cores, 4TB RAM, 0-3 NVIDIA A100 GPUs
* mad06: Milan-X architecture, 128 cores, 1TB RAM, large (768MB) L3 cache

The A100 GPUs are "composable", that is, they can be allocated to different servers upon demand using a Liqid fabric. By default, mad04 and mad05 contain one GPU each (as does login8b). However, should more than 1 GPU be required for a particular workload this can be arranged (at the expense of moving them from the other nodes)

cosma8-shm2 contains:

* ga004: 128 cores, 1TB RAM, AMD MI100 GPU
* ga005: 64 cores, 1TB RAM, 2x AMD MI200 GPU
* ga006: 64 cores, 1TB RAM, 2x AMD MI200 GPU

Should you wish to submit to a particular node, or exclude a partiular node (e.g. to ensure that you have access to a particular type of GPU), you can use the ```bash #SBATCH --exclude=ga004``` directive within your batch script (which in this case would exclude ga004, thus ensuring you have access to a node with 2x AMD MI200 GPUs. Or #SBATCH --nodelist=ga004 (which in this case would submit to only the ga004 node).

## COSMA7 queues: cosma7, cosma7-rp, -pauper and -prince

Access to the DiRAC COSMA7 machine is provided using the two queues cosma7 and cosma7-rp (and their increased or reduced priority versions, cosma7-pauper, cosma7-prince, cosma7-rp-pauper and cosma7-rp-prince). These two queues provide access to half of COSMA7, with 224 nodes in each.  cosma7 uses a 100Gbit/s InfiniBand fabric, while cosma7-rp uses a 100Gbit/s Rockport Ethernet fabric (6D torus topology).

All the queues are configured so that job exclusive access to nodes is enforced. This means that no jobs share a compute node. Therefore, if you only need a single core, your project allocation will still be charged for using 28 cores.

The main use of these queues is for DiRAC projects that have been assigned time at Durham and the mix of jobs expected to match its capabilities are MPI/OpenMP/Hybrid jobs using up to 28 cores per node with a maximum memory of 512GB per node. If any jobs can run using fewer resources than a single node then they should be packaged into a batch job with appropriate internal process control to scale up to this level.

In addition to the hardware limits the queues have the following limits and priorities:


| Name             | Priority          | Maximum run time	   | Maximum cores    |  
| ---------------- | ----------------- | ----------------------| ---------------- | 
| cosma7 and cosma7-rp           | Normal            | 72 hours              | unlimited        | 
| -pauper	   | Low               | 24 hours              | unlimited        | 
| -prince    | Highest           | 30 days               | 4096             | 

The pauper and prince variations of the queues share the same resources so the order that jobs run are decided on a number of factors. Higher priority jobs will run first, and in fact jobs in higher priority queues will always run before lower priority jobs, however, it may not superficially seem like that as jobs from lower priority queues may run as back-fills (this is allowed when a lower priority job will complete before the resources needed for a higher one will become available, so setting a run-time limit for your job may get it completed more quickly). See the [FAQ](faq) for how to make use of back-filling.

## COSMA6 queues: cosma6, cosma6-pauper and cosma6-prince

COSMA6 was retired in April 2023 after 11 years of service.

## COSMA5 queues: cosma, cosma-pauper and cosma-prince, cordelia, cosma-analyse, cosma-bench

Access to the Durham COSMA5 machine is provided using the six queues cosma, cosma-pauper, cosma-prince, cordelia, cosma-analyse and cosma-bench. The first three queues share all the 302 compute nodes dispatching jobs according to the different priorities that the queues have assigned. All the queues are configured so that job exclusive access to nodes is enforced. This means that no jobs share a compute node.

The cordelia queue should be used for single core jobs, and will share computational resources on a single node with other jobs. This allows efficient use of the cluster. When using the cordelia queue, please specify the maximum memory your job will require, e.g.: ```bash #SBATCH --mem=10G``` will reserve 10GB for you, and allow the other cores to use the rest.

The cosma-analyse queue is for data analysis purposes. The cosma-bench queue is for benchmarking.

The main use of these queues is for Durham projects that have been assigned time at Durham and the mix of jobs expected to match its capabilities are MPI/OpenMP/Hybrid jobs using up to 16 cores per node with a maximum memory of 126GB per node. Note that the nodes in COSMA5 are disk-less so this represents a hard memory limit and exceeding this will cause your job to fail. If any jobs can run using fewer resources than a single node then they should be either submitted to the cordelia queue or packaged into a batch job with appropriate internal process control to scale up to this level.

In addition to the hardware limits the queues have the following limits and priorities:

| Name             | Priority          | Maximum run time	     | Maximum cores    |  
| ---------------- | ----------------- | ------------------------| ---------------- | 
| cosma            | Normal            | 72 hours                | unlimited        | 
| cosma-pauper	   | Low               | 24 hours                | unlimited        | 
| cosma-prince     | Highest           | 30 days                 | 4096             | 
| cordelia         | Normal            | 30 days                 | 16               | 
| cosma-bench      | Normal            | 24 hours                | 16               | 
| cosma-analyse    | Normal            | 23 hours, 20 minutes(!) | 144              | 

The three queues share the same resources so the order that jobs run are decided on a number of factors. Higher priority jobs will run first, and in fact jobs in higher priority queues will always run before lower priority jobs, however, it may not superficially seem like that as jobs from lower priority queues may run as back-fills (this is allowed when a lower priority job will complete before the resources needed for a higher one will become available, so setting a run-time limit for your job may get it completed more quickly). See the [Durham utilities](LINK) descriptions for how to make use of back-filling.

cosma queues are exclusive (except cordelia), meaning no matter how many cores you request per node you will have exclusive use of that node. Your allocation will be reduced assuming that you were using all the cores.

The cosma and cosma-pauper queues are available to all users, the -prince queue can only be accessed by special arrangement.

The quarterly allocation can can be found out in the [COSMA usage pages](https://virgodb.cosma.dur.ac.uk/usage/login.php), you'll need your COSMA username, and password or token (generated using the cusagetoken command) to see these.

Jobs within the same queue are scheduled using a fairshare arrangement so each user initially has the same priority. This is then weighted using a resources used formula.

Note that the order of running can again be affected by back-filling (but that will only work if a job is given a run time) and using fewer resources than other jobs.
