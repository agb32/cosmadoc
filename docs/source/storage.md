# Storage

COSMA has multiple storage systems which include:
 - Homespace
 - App space
 - Data space
 - Scratch space
 - Archive space
 - Public space

## Homespace

User homespace is found under /cosma/home and is a NFS-mounted file system.  Users typically have a 10GB quota.  This file system is snapshotted hourly, with snapshots kept for up to one week.  It is also usually backed up daily, with backups kept for up to 60 days.

## App space

User app space is found under /cosma/apps and is a NFS-mounted file system.  Users typically have a 100GB quota.  This file system is snapshotted hourly, with snapshots kept for up to one week.

## Data space

There are multiple data spaces - typically named e.g. /cosma8.  Users typically have a 10TB quota.  These file systems are not backed up but have redundancy.

## Scratch space

There are multiple scratch spaces, ideal for simulation checkpoinging data.  Typically at /snap*.  These file systems have no redundancy and are not backed up.  Therefore they should only be used for data that can be recreated.  These file systems have no user quota, and are cleaned out every 4 months.

## Mounted filesystems

Not all login and compute nodes mount all filesystems. The following table summarizes which filesystems can be read/written from which nodes:

| Filesystem | login5* | m5*** | login7* | m7*** | login8* | m8*** | ????? |
| :--------: | :-----: | :---: | :-----: | :---: | :-----: | :---: | :---: |
| /cosma/home|   rw    |   rw  |   rw    |   rw  |    rw   |   rw  |       |
| /cosma/apps|   rw    |   rw  |   rw    |   rw  |    rw   |   rw  |       |
| /cosma5    |   rw    |   rw  |   rw    |       |    rw   |       |       |
| /cosma7    |   rw    |       |   rw    |       |    rw   |       |       |
| /snap7     |         |       |   rw    |   rw  |         |       |       |
| /cosma8    |         |       |   rw    |   rw  |    rw   |       |       |
| /snap8     |         |       |         |       |    rw   |   rw  |       |
| ???        |         |       |         |       |         |       |       |

# Archive space

The tape archive is a good place for long-term storage and archival of data which is not actively required, or which you wish to back up.  To archive data to tape, please contact cosma-support.

# Public space

There are multiple ways in which you can make data publicly accessible.  We have a [StorJ](storj.md) object storage system hosted on servers spread across DiRAC, which can be used for uploading data and storing with users.

It is also possible to make individual files available for download via a web link, please ask if you wish to do this.
