# The DAOS file system

The DAOS file system is based on 4 nodes each with 8x NVMe drives, and a total capaciy of around 48TB.

It is an experimental file system, only accessible on the DINE system.

# DAOS USER instructions



DAOS access: Currently you will not be able to access the DAOS file system from any of the normal login nodes.

DAOS is only available on the bluefield node b101-b114, and b116. To use daos consider b116 as a login node, so ssh to b116 then you should be able to access your DAOS filesystem, and its associated data before and after you run your jobs. 

1. Before you use the DAOS system: Access to the DAOS filesystem is via a DAOS pool. Pools can only be created or amended by a sysadmin. Currently the only pool that exists is called DAOS8 and is 47TP in size, and is accessible for anyone who is part of the durham group. If you are part of that group then please have a go, otherwise contact the sysadmin team and we can add you to the DAOS8 pool.

2. Create a container for your data: Think about this as a directory that you can place (mount) at different places in the file system. In this example I will mount my container in my home directory.
So we are going to create a container called “PiData”, and this container will be created in the pool named DAOS8. I am trying to give my container a name that I and anyone else who looks at in the DAOS8 pool will understand what is inside this container. The container will have a POSIX file system type, and we want to create this container with some redundancy, so I will add rf:1. This means there will always be an additional data copy erasure code (i.e. 1 disk failure).  You might wish to use rf:2 to allow for simultaneous failure of two disks.

`daos cont create DAOS8 --label PiData --type POSIX --properties rf:1`

You will be informed that the container was created. 

3. Confirm container creation:If you would like to confirm this, then you can list all the containers that exist in the DAOS8 pool.

```
daos cont list DAOS8
 UUID                                 Label     
----                                 -----     
76ad9d89-1b21-4613-85bb-f23848f2db7e PiData    
6d4ce6ec-4c35-435b-90dd-0fb60a18dcb2 contTest1
```

This shows the new container PiData, and another container that was used during testing.

4. Create a local mount point: To access this container you need a place on the file system where you would like to access that data. I will create a local director and then mount the container there.

```
mkdir PiData
dfuse -m ./PiData --pool DAOS8 --cont PiData
```

In this case I named the container and the directory the same, but you can call them different names.

If you ‘ls’ to see what is inside the container it should be empty as we have not used it before.

```
ls ./PiData
```

5. Using this container within your job script: Within your job script you need to mount the container on the compute node before you try to access it, and then unmount the container afterwards. This will ensure you never have any stale mounts if you use the same compute node in the future. So with in you job script add the following lines:

```
## mount your container
mountPoint="/cosma/home/sfw/DAOS/PiData"
#
dfuse -m ${mountPoint} --pool DAOS8 --cont PiData

## Add you program here
echo `date`" -2- "`hostname` >> ${mountPoint}/PiData.log
tail ${mountPoint}/PiData.log

## unmount your container
fusermount3 -u ${mountPoint}
```

6. Exemplar script: Below is a working script

```
#!/bin/bash -l

#1 node, runing 1 core.

#SBATCH --ntasks 1        # The number of cores you need...
#SBATCH -J Daos-PiData_01 #Give it something meaningful.
#SBATCH -o standard_output_file.%J.out
#SBATCH -e standard_error_file.%J.err
#SBATCH -p bluefield1     #or some other partition, e.g. cosma, cosma6, etc.
#SBATCH -A durham         #e.g. dp004
#SBATCH --exclusive
#SBATCH -t 0:01:00        # Max time expected for code to run, 1 minute
#SBATCH --nodes=1         # Number of nodes to use
#SBATCH --nodelist=b101   # Specific node. for DAOS this is b101- b114
#SBATCH --mail-type=END   # notifications for job done & fail
#SBATCH --mail-user=richard.regan@durham.ac.uk 

#module list

#mount container
mountPoint="/cosma/home/sfw/DAOS/PiData"

dfuse -m ${mountPoint} --pool DAOS8 --cont PiData

## Add your program here
echo `date`" -- "`hostname` >> ${mountPoint}/PiData.log
tail ${mountPoint}/PiData.log

## unmount container
fusermount3 -u ${mountPoint}
```

If you run this script then the output file will show that it ran successfully and show the date and host name. Great it works, but if you try to view this locally mounted container you will not see the update.

7. Seeing your data: To ensure you see the updated date you need to unmount and then mount the container.

```
fusermount3 -u ./PiData
dfuse -m ./PiData --pool DAOS8 --cont PiData
```

Now any update in the container and its associated file will be visible to you.


