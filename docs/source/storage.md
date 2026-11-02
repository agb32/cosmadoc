# Storage

COSMA has multiple storage systems which include:
 - Homespace
 - App space
 - Data space
 - Scratch space
 - Temporary space
 - Archive space
 - Public space

## Homespace

User homespace is found under /cosma/home and is a NFS-mounted file system.  Users typically have a 10GB quota.  This file system is snapshotted hourly, with snapshots kept for up to one week.  It is also usually backed up daily, with backups kept for up to 60 days.

## App space

User app space is found under /cosma/apps and is a NFS-mounted file system.  Users typically have a 100GB quota.  This file system is snapshotted hourly, with snapshots kept for up to one week.

## Data space

There are multiple data spaces - typically named e.g. /cosma8.  Users typically have a 10TB quota.  These file systems are not backed up but have redundancy.

## Scratch space

There are multiple scratch spaces, ideal for simulation checkpointing data.  Typically at /snap*.  These file systems have no redundancy and are not backed up.  Therefore they should only be used for data that can be recreated.  These file systems have no user quota, and are cleaned out every 4 months.

## Temporary space

Every node has its own /tmp, which can only be seen from that node.  It works differently on login nodes and compute nodes:

| Nodes | What /tmp is | Size | Can run programs from it? | Files are deleted after |
| ----- | ------------ | ---- | ------------------------- | ----------------------- |
| Login nodes, mad06 | Memory (tmpfs), shared by all users | 100GB | No | 3 days without changes |
| Compute nodes, and other nodes for direct ssh | Local disk | 21GB to 1.4TB, see below | Yes | 10 days without use |
| gn002, gn003 | Part of the system disk | 800GB, shared with the operating system | Yes | 10 days without use |

Local disk sizes, measured on one node of each type in October 2026:

| Size | Nodes |
| ---- | ----- |
| 21GB | cosma7-rp |
| 43GB | cosma7, cosma8, bluefield1, cosma7-shm |
| 88GB | cosma5, dine2, cosma8-shm, cosma8-shm2, cosma8-shm3, cosma8-ska, gn001, gn004, gn005 |
| 177GB | mad11, mad12, ga008 |
| 1.4TB | gi001 |

Sizes can differ between nodes, so to see the size and free space on the node you are using, run `df -h /tmp`.

There is no per-user quota on /tmp, so one user can fill it for everyone on that node.  For large temporary files, use your space on /cosma* or /snap* instead.

### /tmp on login nodes

Because /tmp is held in memory on login nodes, large files take memory from other users.  Programs in /tmp cannot be run, and fail with `Permission denied`.  If a tool needs to run something from its temporary directory, point it at your app space instead:

```
mkdir -p /cosma/apps/PROJECT/USERNAME/tmp
export TMPDIR=/cosma/apps/PROJECT/USERNAME/tmp
```

### /tmp in batch jobs

Slurm does not create a private temporary directory for each job, and does not set `TMPDIR`:

- /tmp is shared with any other jobs on the node.
- Files stay in /tmp when your job ends, so please delete them.
- In a multi-node job, each node has a separate /tmp.

To use a private directory that is removed when your job script exits, add this to your job script:

```
export TMPDIR=$(mktemp -d /tmp/$USER.XXXXXX)
trap 'rm -rf "$TMPDIR"' EXIT
```

### /dev/shm

/dev/shm is held in memory on every node, and is shared by all users.  In a batch job, files that you write there count towards your job's memory limit, so your job can be killed with an out of memory error if you do not request enough.  Files stay in /dev/shm when your job ends, so please delete them.

## Mounted filesystems

Not all login and compute nodes mount all filesystems. The following table summarizes which filesystems can be read/written from which nodes:

| Filesystem | login5* | m5*** | login7* | m7*** | login8* | m8*** |
| :--------: | :-----: | :---: | :-----: | :---: | :-----: | :---: |
| /cosma/home|   rw    |   rw  |   rw    |   rw  |    rw   |   rw  |
| /cosma/apps|   rw    |   rw  |   rw    |   rw  |    rw   |   rw  |
| /cosma5    |   rw    |   rw  |   rw    |       |    rw   |       |
| /cosma7    |   rw    |   r   |   rw    |   rw  |    rw   |   r   |
| /snap7     |         |       |   rw    |   rw  |         |       |
| /cosma8    |   rw    |       |   rw    |       |    rw   |   rw  |
| /snap8     |         |       |         |       |    rw   |   rw  |
| /cosma6    |   rw    |       |   rw    |       |    rw   |       |

In these tables, rw means read and write, r means read-only, and a blank means that the file system is not available.  /cosma/home and /cosma/apps are available everywhere, including on the nodes below.

Other nodes and queues:

| Nodes                         | /cosma5 | /cosma7 | /cosma8 | /snap7 | /snap8 |
| :---------------------------: | :-----: | :-----: | :-----: | :----: | :----: |
| mad06, gn001, gn005, gi001    |   rw    |   rw    |   rw    |        |   rw   |
| mad11, mad12, gn002           |   rw    |   rw    |   rw    |        |        |
| gn004                         |   rw    |   rw    |   rw    |   rw   |   rw   |
| ga008                         |         |   rw    |   rw    |        |        |
| cosma8-shm, cosma8-shm2, cosma8-ska | rw |  rw    |   rw    |        |   rw   |
| cosma7-shm                    |   rw    |   rw    |   rw    |   rw   |        |
| dine2                         |         |   r     |   rw    |        |   rw   |
| bluefield1, gracehopper       |   rw    |   rw    |   rw    |        |        |

To check a file system on any other node, run this on that node.  It prints rw or ro, followed by other mount options, or nothing if the file system is not available:

```
findmnt -n -T /cosma7/data -o OPTIONS
```

# Archive space

The tape archive is a good place for long-term storage and archival of data which is not actively required, or which you wish to back up.  To archive data to tape, please contact cosma-support.

# Public space

There are multiple ways in which you can make data publicly accessible.  We have a [StorJ](storj.md) object storage system hosted on servers spread across DiRAC, which can be used for uploading data and storing with users.

It is also possible to make individual files available for download via a web link, please ask if you wish to do this.
