
# COSMA job queues

A list of available queues can be found using the `sinfo -a -s` command.  Partitions are summarised here:

| Partition | Nodes | Node details | GPU info | Network | Comments |
| --------- | ----- | ------------ | -------- | ------- | -------- |
| cosma8    | 528, m8001-m8528   | 128 cores, 1TB | No | HDR 200g | Variants: -rome, -milan, -prince, -pauper, -serial |
| cosma7    | 220, m7229-m7448  | 28 cores, 512GB | No | EDR 100g | Variants: -prince, -pauper |
| cosma7-rp | 222, m7001-m7222  | 28 cores, 512GB | No | Rockport 100g | Variants: -prince, -pauper |
| cosma8-shm | 2, mad04,05 | 128 cores, 4TB | Up to 3x A100 | HDR 200g | Composible fabric |
| cosma8-shm2 | 2, ga004,06 | 128,64 cores, 1TB | MI100, 2x MI210 | HDR 200g | AMD GPUs |
| cosma8-shm3 | 2, mad08,09 | 192 cores, 768GB | No | HDR 200g | AMD Genoa |
| cosma8-ska | 1, mad07 | 56 cores, 4TB | No | HDR 200g | NVDIMMs |
| cosma8-ska2 | 4, mad01,03,04,05 | 56, 48, 128, 128 cores, 3, 6, 4, 4TB | 3x A100 | EDR/HDR | mad04,05 composible fabric |
| cosma8-highram | See cosma8-shm |
| cosma8-draper | 1, ga007 | 96 cores, 2TB| 8x MI300X | HDR200 | AMD GPU |
| cosma8-dine2 | 8, gc001-gc008 | 64 cores, 2TB | A30, V100 | HDR200 | Composible fabric |
| cosma7-mad | 1, mad01 | 56 cores, 3TB | No | EDR 100g |
| cosma7-shm | 2, mad01,02 | 56, 112 cores, 3, 1.5TB | No | EDR 100g |
| cosma7-shm2 | 1, mad03 | 48 cores, 6TB | No EDR 100g | NVDIMMs |
| cosma5 | 8, m5001-m5008 | 256 cores, 1.5TB | No | EDR 100g | Replacement of original COSMA5 |
| cosma-analyse | 3, mad01,02,03 | 56,112,48 cores, 3,1.5,6TB | No | EDR 100g |
| bluefield1 | 18, b101-b124 with gaps | 32 cores, 512G | No | HDR200 | Including Bluefield2 DPUs |
| dine | See bluefield1 |
| dine2 | See cosma8-dine2 |
| gracehopper | 1, gn003 | 72 cores, 512GB | H100 GPU | HDR200 | Arm CPU |
| mi300x | See cosma8-draper |

Nodes available for direct SSH (from a login node), for prototyping etc:
* gn002 - Grace Hopper, cf gracehopper parttion
* mad06 - 128 cores, 1TB RAM, Milan-X (large cache), part of the cosma8-shm composible fabric with up to 3 A100 GPUs
* ga008 - 96 cores, 500G, 4x AMD MI300A GPUs



## COSMA8 queues

There are a number of COSMA8 queues: cosma8, cosma8-prince, cosma8-pauper, cosma8-serial, cosma8-shm, cosma8-shm2, cosma8-shm3, cosma8-draper, cosma8-dine2, cosma8-milan, cosma8-rome, cosma8-highram  (and a few others)

If you are unsure, submit to cosma8 (assuming yuo have access - [see below](#access-to-cosma8)).

Because COSMA8 contains two generations of processors (Rome and Milan), if you want to only submit to one of those (there is a 10-20% performance difference between them), you can submit to the specific cosma8-milan or cosma8-rome partitions.

If your job does not require a full node (of 128 cores), you can submit to the cosma8-serial queue.

If you have a valid reason for a longer running time (than 3 days), or for higher priority, you can ask to be able to submit to the `-prince` queues.  The prince queues allow 30 day run times, and can be used by large jobs to avoid the need for reservations and increase system efficiency.

The -pauper queues are for low priority jobs, primarily for projects who have used up their allocation (who will automatically be demoted to this queue).  They are limited to a 24 hour runtime.

Other COSMA8 queues are smaller specialised compute partitions, mentioned in more detail below.

### Access to COSMA8

You can use the `scontrol show partition=PARTITION` to show details about each queue, and work out which groups/projects you would need to be in to submit jobs to them.

Access to the DiRAC COSMA8 system is only for DiRAC projects with a time allocation on this system. Each COSMA8 compute node has 128 cores and 1TB RAM. If you request fewer than 128 cores for a job using the cosma8-serial queue, you will not be granted exclusive access to a node, and therefore may share a node with other jobs. Unless you specify a memory in your SLURM script (e.g. ```bash #SBATCH --mem=800G```), then you will be given a fraction of 1TB equal to the number of cores you request/128. If you do not wish to share a node, use the "#SBATCH --exclusive" flag (or don't submit to the cosma8-serial queue). The cosma8-shm queue provides access to two large 4TB nodes, each with 128 cores.


## cosma8-shm, cosma8-shm2, cosma8-shm3

The cosma8-shm and cosma8-shm2 queues are small queues with non-standard hardware.

### cosma8-shm contains:

* mad04: 128 cores, 4TB RAM, 0-3 NVIDIA A100 GPUs, AMD Rome processors
* mad05: 128 cores, 4TB RAM, 0-3 NVIDIA A100 GPUs, AMD Rome processors

If also used to include mad06: Milan-X architecture, 128 cores, 1TB RAM, large (768MB) L3 cache, with 0-3 NVIDIA A100 GPUs, though this is now a more general purpose node for direct ssh from a login node.

The A100 GPUs are "composable", that is, they can be allocated to different servers upon demand using a Liqid fabric. By default, mad04 and mad05 contain one GPU each (as does login8b). However, should more than 1 GPU be required for a particular workload this can be arranged (at the expense of moving them from the other nodes)

### cosma8-shm2 contains:

* ga004: 128 cores, 1TB RAM, AMD MI100 GPU, AMD Rome processors
* ga005: 64 cores, 1TB RAM, 2x AMD MI200 GPU, AMD Rome processors
* ga006: 64 cores, 1TB RAM, 2x AMD MI200 GPU, AMD Rome processors

Should you wish to submit to a particular node, or exclude a particular node (e.g. to ensure that you have access to a particular type of GPU), you can use the ```bash #SBATCH --exclude=ga004``` directive within your batch script (which in this case would exclude ga004, thus ensuring you have access to a node with 2x AMD MI200 GPUs. Or #SBATCH --nodelist=ga004 (which in this case would submit to only the ga004 node).

### cosma8-shm3 contains:

* mad08: 192 cores, 768GB RAM, Genoa processors
* mad09: 192 cores, 768GB RAM, Genoa processors

### cosma8-highram

The cosma8-highram queue uses the same nodes as the cosma8-shm queue, but is for DiRAC projects.

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

## COSMA5 queues: cosma5, cosma-test

Access to the Durham COSMA5 machine is provided using the cosma5 queue. This queue is comprised of the new (2024, 2025) COSMA5 nodes, a total of 8 nodes each with 256 cores and 1.5TB RAM.  This partition is non-exclusive, i.e. jobs will share a node with other jobs unless exclusive access is explicitly requested.  You are therefore advised to explicitly request the amount of RAM your job will use, otherwise a default of around 6GB per core will be allocated.

The old COSMA5 nodes were retired in 2025, originally starting service in 2012 (16 cores per node, 128GB RAM).  There were originally 420 nodes, 6720 cores.

The main use of this queue is for Durham projects that have been assigned time at Durham and the mix of jobs expected to match its capabilities are MPI/OpenMP/Hybrid jobs using up to 256 cores per node with a maximum memory of 1.5TB per node.

In addition to the hardware limits the queues have the following limits and priorities:

| Name             | Priority          | Maximum run time        | Maximum cores    | Cores per node | nodes | RAM per node |
| ---------------- | ----------------- | ------------------------| ---------------- | ---------------| ------| -------------|
| cosma5           | Normal            | 72 hours                | unlimited        | 256            | 8     | 1.5TB        |

The cosma5-test queue is for testing purposes only.

Higher priority jobs will run first, though lower priority jobs with shorter runtimes may run as back-fill jobs, making use of available nodes before a larger job is due to start.  Setting a run-time limit for your job may get it completed more quickly. See the [FAQ](faq) descriptions for how to make use of back-filling.

The quarterly allocation can can be found out in the [COSMA usage pages](https://virgodb.cosma.dur.ac.uk/usage/login.php), you'll need your
COSMA username and password to see these.  However, COSMA5 is no longer listed here as no DiRAC allocations are awarded on it.

Jobs within the same queue are scheduled using a fairshare arrangement so each user initially has the same priority. This is then weighted using a resources used formula.

Note that the order of running can again be affected by back-filling (but that will only work if a job is given a run time) and using fewer resources than other jobs.

## cosma8-ska, cosma8-ska2 queues

The cosma8-ska and cosma8-ska2 queues are for SKA projects.

cosma8-ska is a single node (mad07) with 4TB RAM and 128 cores.

cosma8-ska2 has 4 high RAM nodes (mad01, mad03, mad04, mad05), with 3, 6, 4 and 4TB RAM respectively, and between 56-128 cores.

## cosma8-draper and mi300x queues

The cosma8-draper and mi300x queues both contain the same single node, an 8-GPU system containing 8x MI300X GPUs.

Direct access to an MI300A system (4x GPUs) is available via direct ssh to ga008 from a login node.

The cosma8-draper queue is named in honour of Peter Draper, who retired from COSMA technical support after many years in 2026.

## cosma8-dine2, dine2

The cosma8-dine2 and dine2 partitions contain 8 nodes each with 2TB RAM and 64 cores (Intel Sapphire Rapids).  Each node also contains between 0-12 GPUs: This is a composible system where GPUs can be allocated to nodes upon request.  There are a total of 8x A30 GPUs and 4x V100 gPUs.

## cosma7-mad

A single node, mad01, with 56 cores and 3TB RAM

## cosma7-shm

Two nodes, mad01, mad02, with 56 and 3TB RAM and 112 cores and 1.5TB RAM respectively.

## cosma7-shm2

A single node, mad03, with 48 cores and 6TB RAM

## cosma-analyse

A partition for analysis of cosmological datasets, including mad01 (56 cores, 3TB), mad02 (112 cores, 1.5TB), mad03 (48 cores, 6TB).

## bluefield1, dine

Both are 18 node (was 24) partitions with each node having 32 cores and 512GB RAM.  This includes gitlab-runners, and so can be used for CI/CD.  The nodes are b[101-105,107-115, 116-119]

## gracehopper

A single Grace-Hopper node, gn003.  The gn002 node is also Grace-Hopper, available for direct ssh from a login node for code testing, development, etc.

## Other queues

There are a number of other queues which may be of relevance.  If in doubt, please ask.
