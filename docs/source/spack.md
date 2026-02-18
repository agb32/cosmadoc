# Spack Package Environment

The [Spack](http://spack.readthedocs.io) package management tool is used
to manage some of the software and libraries installed on COSMA, 
please use it and report any issues or any feature requests.

Spack allows us to automatically resolve dependencies and have multiple versions of tested
software installed simultaneously without them interfering with each other.

To achieve this, Spack makes use of RPATH to hard-code the paths of dependencies
into libraries. This means that when you load a module for a particular library
you do not need to load any further modules for dependencies of that library.

## Activating Environments 

You can use created environments using ```module  load spack```

This will print some commands which you should then execute depending which cosma machine you are using.



