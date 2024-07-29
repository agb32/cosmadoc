# File system access control lists

The Lustre file systems on COSMA have extended attribute support such that access control lists can be used for fine-grained control of file access.

By default, POSIX file system control is defined by user, group and world permissions, which can be read, write or execute.

To give a specific user read access to a file, you can use:

```
#for the user USER:
setfacl -m USER:r /path/to/file
```

Permissions can also be revoked, e.g.:

```
setfacl --modify=USER:--- /path/to/file
```

The `getfacl` command can be used to see current permissions.
