# Using Python on COSMA

There are a number of different Python versions available on COSMA.  You can see these using the `module available python` and `module available anaconda` commands.  To select one of these, you can `module load python/VERSION`.  At this point, running the `python` command (or in some cases `python3`) will give you your selected Python interpreter.

If you need a newer version of Python than is available, please ask cosma-support.

## Python libraries

The installed versions of Python generally have a limited number of libraries installed.  Therefore, if you have a requirement for additional libraries, you will need to install them yourself in a virtual environment.

### Installing Python libraries

To install python libraries, the following steps can be used:

0. module load the Python you wish to use (e.g. `module load python/3.12.4`).
1. Create a virtual environment: `python -m venv /path/to/myenv`.  /cosma/apps/PROJECT/USERNAME is a good place for this.
2. Activate the virtual environment: `source /path/to/myenv/bin/activate`
3. Install the packages you require: `pip install mypackage`
4. Run Python: `python`

If you log in with a different session and want to use this environment, you will need to remember to activate it: `source /path/to/myenv/bin/activate`

Once you have finished, you can deactivate your environment: `deactivate`

If you wish to remove it permanently, you can `rm -r /path/to/myenv`

You can have multiple virtual environments.  This allows you to install specific library versions according to your requirements.

#### Compiled modules

If the library you are pip installing requires compiling, you may need to load a C compiler module, and possibly various othe libraries (e.g. MPI, FFTW, HDF5, etc).

It is usually best to use the compiler that the Python interpreter you are using was compiled with.  To find that out, start the Python interpreter, and the information lines will tell you which compiler to use.

Other compilers may offer improved performance, and you can experiement with these.
