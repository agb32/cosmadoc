# The Lustre file system

/cosma5, /cosma7, /cosma8 and /snap7, /snap8 are LUSTRE file systems. These
are parallel file systems which can write different parts of a file to
different physical hard drives, thereby speeding up read and write access.

By default, Lustre is configured to write files to a single logical hard
drive. However, for large files (typically >100MB), improved performance can
be achieved if the file is striped across multiple disks. This must be
performed when the file is first created: It is not possible to re-stripe a
Lustre file (though the file can be migrated).  Alternatively, striping can be
set on a directory, meaning that all new files within that directory will be
striped.

It is possible to set up a "progressive file layout", automatically increasing
the number of stripes as file size grows.


Lustre files inherit their striping from the directory in which they are
written. Therefore if you have a data directory containing only large files,
the simplest method to stripe these files is to simply stripe the directory
when it is created (i.e. before any files are written to it).

To stripe a directory:

    lfs setstripe -S 4M -c -1 /path/to/directory

which will stripe across all disks, in 4MB chunks.

To stripe a file before it is created (i.e. to touch it):

    lfs setstripe -S 4M -c -1 /path/to/new/file

This will create an empty file, which can then be written to.

For very large files, striping is essential if the file won't fit on a single logical drive.

A C API also exists, so that striping can be performed
programmatically. However, don't reinvent the wheel, and use e.g. parallel
HDF5 instead (with correct settings).

The Lustre file systems also allow progressive striping (striping larger files
more, automatically). This is easy to set up, but please refer to Lustre
documentation for more details.

It should be noted that there is a maximum size of less than 4GB when setting
the stripe size (i.e. -S 4G won't work), and that striping too wide can lead
to problems (e.g. -c -1 is not a good idea on /snap8).

## Redundancy

The /snap7 and /snap8 file systems have no built in redundancy, and so if a
disk fails, data will be lost. However, it is possible to set up RAID-1
(mirroring) for data protection on a per-directory or a file-by-file
basis. The lfs mirror command can be used to do this. For example, to mirror a
directory to 2 disks:

    lfs mirror create -N -p pool1 -N -p pool2 mirroredDirectory/

Other options can be added to this, to set striping etc:

    lfs mirror create -N -p pool1 -c 2 -N -p pool2 -c 2 /mirroredStripedDirectory/

(the -c 2 means to strip across 2 disks for each mirror)

Note, it is important to use the -p pool1/2 option as otherwise it is possible
for both mirrors of a file to be on the same disk (which obviously is not
ideal for redundancy!)

More advanced options are available, for example multiple mirrors, different
striping on different mirrors, etc.

Once you have written a file, you need to manually synchronise it:

    lfs mirror resync file1

If you have many files, they can be done at the same time, e.g.:

    lfs mirror resync *

To check files, you can use lfs mirror verify file1.

If you are using the /snap file systems for restart/checkpoint files, please
ensure that you either mirror, or alternatively, copy occasionally to /cosma7
or /cosma8 (as appropriate). It will not usually be necessary to copy every
set of restart files, but advisable to copy every few days to minimise wasted
compute time in the event that files are lost. While copying these files,
please be sure to maintain consistency, i.e. do not overwrite an old set until
the new set has been copied across and verified.

## Rsync

If you are rsync-ing data from elsewhere onto the Lustre file system, and have
files >1GB in size, the rsyncLustre module should be used. This is a patched
version of rsync which will automatically stripe all files >1GB in size.

## Directory sizes

To find the size of everything within a directory, you can use the standard
`du` command.  e.g. `du -s -h /cosma8/data/PROJECT/USER`.  However, for
directories with many files, this can take a long time.  Note, this returns
the size of the files on disk, after compression.  To return the sum of actual
file size (i.e. if you were to transfer to another system without
compression), you can add the `--apparent-size` option.

A faster way, which only touches the Lustre metadata servers, not the object
storage servers, is to use `lfs find`.  For example:

```
lfs find /cosma8/data/PROJECT/USER --lazy --printf "%s\n" | awk '{sum+=$1;n+=1}END{print "Total: "sum" bytes, "sum/1024/1024/1024" GB, "n" files"}'
```

# Quotas

Quotas on the Lustre file system can be found using

```
lfs quota -u USERNAME -h /FILESYSTEM
e.g.
lfs quota -u dc-cosma -h /cosma8
```

Or (with the `cosma` module loaded), using the `lfsquota` command (which will
show you your quota on all attached Lustre file systems). The quota of your
project can be found using

```
lfs quota -g GROUP -h /FILESYSTEM
```

or using `lfsquota -g GROUP`.

# Finding out who is using the group quota.

The usage pages are described in [Usage](system.md#system-usage). These have
this information for all the lustre file systems. Note this is only updated
each night or once per week for some types of information, so may be out of
date if you want to know this minute.

## Access permissions

File access permissions can be managed using [access control lists](acl.md).
