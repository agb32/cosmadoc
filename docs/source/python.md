# Using Python on COSMA

There are a number of different Python versions available on COSMA.  You can see these using the `module available python` and `module available anaconda` commands.  To select one of these, you can `module load python/VERSION`.  At this point, running the `python` command (or in some cases `python3`) will give you your selected Python interpreter.

If you need a newer version of Python than is available, please ask cosma-support.

## Python libraries

The installed versions of Python generally have a limited number of libraries installed.  Therefore, if you have a requirement for additional libraries, you will need to install them yourself in a virtual environment.

### Installing Python libraries

To install python libraries, the following steps can be used:

1. Create a virtual environment: `python -m venv /path/to/myenv`
2. Activate the virtual environment: `source /path/to/myenv/bin/activate`
3. Install the packages you require: `pip install mypackage`
4. Run Python: `python`

If you log in with a different session and want to use this environment, you will need to remember to activate it: `source /path/to/myenv/bin/activate`

Once you have finished, you can deactivate your environment: `deactivate`

If you wish to remove it permanently, you can `rm -r /path/to/myenv`

You can have multiple virtual environments.  This allows you to install specific library versions according to your requirements.
