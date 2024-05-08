# Storage

COSMA has multiple storage systems which include:
 - Homespace
 - Data space
 - Scratch space
 - Archive space

## Homespace

User homespace is found under /cosma/home and is a NFS-mounted file system.  Users typically have a 10GB quota.

## Data space

There are multiple data spaces - typically named e.g. /cosma8.  Users typically have a 10TB quota.  These file systems are not backed up but have redundancy.

## Scratch space

There are multiple scratch spaces, ideal for simulation checkpoinging data.  Typically at /snap*.  These file systems have no redundancy and are not backed up.  Therefore they should only be used for data that can be recreated.  These file systems have no user quota, and are cleaned out every 4 months.

## Archive space

The tape archive is a good place for long-term storage and archival of data which is not actively required, or which you wish to back up.  To archive data to tape, please contact cosma-support.
