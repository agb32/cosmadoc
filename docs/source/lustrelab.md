# The Lustre lab

The Hardware Lab includes multiple Lustre file systems, mostly in production in COSMA, but some experimental.

## File system details

### /cosma8

Comprised of:

- 4 metadata servers (MDSs)
  - Operating in HA pairs (manual failover)
  - Each with 4x 6.4TB NVMe drives (internal)
    - Two RAID1 pairs
    - Synced to a corresponding pair using DRBD
    - One metadata target (MDT) per MDS in normal operation
      - Up to two during failover
  - ldiskfs
  
- 20 object storage servers (OSSs)
  - Operating in HA pairs (manual failover)
  - Each with 168x 16TB drives attached
    - Two ME484 JBODs, accessed by each server in the pair
  - 7 object storage targets (OSTs) per OSS
    - Up to 14 during failover
  - ZFS

### /cosma7

- 2 MDS
  - Shared Powerstore RAID controller
    - Providing one MDT per server
  - ldiskfs
- 4 OSS
  - Pair together for manual HA
  - Each pair accessing a pair of ME5084 RAID controllers
    - 84x 16TB drives in each controller
    - Providing 2 OSTs per server
  - ldiskfs
  
### /cosma5

- 1 MDS/OSS
- 1 OSS
- 168 drives shared between them, 12TB
- ZFS for OSTs and MDTs
  - MDTs are RAID1 with no HA

### /cosma6

Repurposed hardware from the old /cosma6 storage

- 1 MDS
  - And one cold spare
  - ldiskfs
- 3 OSSs
  - And one cold spare
  - ZFS
- 3 ME484 JBODs
- 1 SSD RAID controller for MDTs
  - A single point of failure

An interesting setup with each server connected to two JBODs, allowing failure of any server or any JBOD.

Care must be taken with multipath labelling when replacing disks in this system.

### /snap7

An ultra-fast NVMe-based file system with:

- 1 MDS
  - 1 MDT (ldiskfs)
- 20 OSS
  - 8 OSTs each (single 3.2TB NVMe disks, ldiskfs)

This file system has no redundancy in the OSTs (if a disk fails, that OST will be lost.  Achieving read/write speeds of around 200GByte/s, this is believed to have been the fastest file system in Europe at the time of installation.

### /snap8

A similar design to /snap7, with:

- 1 MDS
  - 4 MDTs (each a RAID1 pair of NVMe drives, ldiskfs)
- 24 OSSs
  - 8 OSTs each ( single 6.4TB NVMe disks, ldiskfs)

Read and write speeds up to around 400GByte/s have been measured.

The /snap file systems are designed with a capacity equal to approximately twice the cluster RAM, to enable two memory snapshots (simulation checkpoints) to be stored simultaneously.

## Monitoring

We use a Lustre node exporter and grafana to monitor the Lustre file systems.

## The Lustre journey

All systems are self-installed and managed using vanilla opensource Lustre.

### Exciting incidents!

Hardware and software sometimes fails.  Here we document some of the interesting times we have had with Lustre.

#### The COSMA8 incident, autumn 2021

A disk failure, which should have been routine, caused a zpool to lock itself.  At the time, pacemaker was configured for automatic failover.  This then kicked into action since Lustre was unable to write to the frozen pool.  When the pool started up on the HA pair, again it couldn't be written to, and so HA failed over again.  This destroyed the zpool, and data was lost.

Fortunately, this was just after commissioning, so the amount of data lost was small and could be compensated for.

We then disabled pacemaker on all our Lustre systems.

#### MDT Raid controller failuures, January 2026

Two raid failures in the space of two weeks.

The first one was fine: DRBD continued to work in diskless mode, replicating data onto the correctly working server.  The fix was fairly simple:

- umount the MDT
- demote DRBD to secondary
- promote DRBD to primary on the HA pair
- mount the MDT on the HA pair
- run an lfsck

The server was then rebooted, and the raid controller came back to life.  This process was then reversed to fail back over.

A raid card in another server then failed less than two weeks over.  Upon following the previous recipe, the MDT failed to mount on its HA pair, indicating that the underlying ldiskfs (ext4) filesystem had been corrupted.

An e2fsck was performed which identified and removed some file system inconsistencies.

Again, the MDT failed to mount, with the messages file showing a key message:  `can't open oi.16.6`.  This is an internal Lustre file, and must have been corrupt.

The instructions for a backend file system level backup was then partly followed, but primarily this involved, after unmounting all Lustre clients:

- Mounting the device as an ldiskfs file system (`mount -t ldiskfs /dev/mdt3 /mnt/tmp`).
- Removing files here: `rm -rf oi.16* lfsck_* LFSCK CATALOGS`
- Unmounting the device
- Mounting as a Lustre mdt mount (`mount -t lustre /dev/mdt3 /mnt/tmp`).

An `lctl lfsck` was then performed to repair any inconsistencies.  This took around four hours, repairing some layout and namespace elements.  We think that it is unlikely that any user data was lost.

