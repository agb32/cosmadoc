# The module environment

The Environment Modules package is a tool that simplifies shell
initialization and lets users easily modify their environment. Modules
can be loaded and unloaded during shell startup (i.e. in
.bash_profile), in queue submission scripts, or dynamically during an
interactive shell session. Loading a module simply changes environment
variables.

An experimental [Spack install](/spack.md) is also available.

Common module commands include:

*    ```module list```: lists currently loaded modules
*    ```module load XYZ```: loads the default version of the XYZ module
*    ```module load XYZ/1.0.0```: loads the 1.0.0 version of the XYZ module
*    ```module unload```: unloads the XYZ module
*    ```module purge```: unloads all currently loaded modules
*    ```module av```: lists all available modules
*    ```module av XYZ```: lists all available version of the XYZ module
*    ```module save NAME```: saves the current module state to a name of your choice
*    ```module restore NAME```: restores a module state previously saved (using files in ~/.module)

While loading some modules, their dependencies must be loaded as well. For instance, loading fftw module requires at least one compiler module (such as gnu_comp or intel_comp) to be loaded.

For more information, type man module or go to the [project website](http://modules.sourceforge.net).

If you are unsure what a good combination of modules is for a specific
software tool, please ask cosma-support, or view the code pages.

The `module save` and `restore` commands are good ways of quickly swapping between favourite module environments.
