# Using VS Code with COSMA

Although we would recommend Emacs, many users prefer VS Code.  The following guidance is under review, and if you spot anything that could be changed, please let us know or put in a pull request.

## Install VS Code

Install Visual Studio Code on your local computer.

You’ll also want the Remote - SSH extension from Microsoft. It allows VS Code to connect directly to the HPC login node over SSH.

## Make sure SSH works

First, test the HPC connection from a normal terminal:

ssh -i /path/to/ssh/key username@loginX.cosma.dur.ac.uk

Replace the hostname and username with those relevant for you.

## Configure VS Code

In VS Code:

- Install Remote - SSH.
- Open the Command Palette with Ctrl+Shift+P (Cmd+Shift+P on macOS).
- Select Remote-SSH: Connect to Host...
- Enter the COSMA login node and your ssh key

VS Code will establish an SSH connection and install its remote components on the HPC system.  Using your /cosma/apps space is good for this.

A new VS Code window will open. The bottom-left corner should indicate that you are connected to the remote machine.

## Open your project

Once connected, use:

File → Open Folder

and select your project directory on the HPC filesystem, for example:

/cosma/home/project/your_username/my_project

You can now edit files as though they were local files, but the files actually reside on the HPC system.

## Use the integrated terminal

Open:

Terminal → New Terminal

The terminal is running on the HPC system, so commands such as:

```
pwd
ls
module avail
```

are executed remotely.

Modules also work:

```
module load python
python my_script.py
```

## Don't normally run heavy jobs on the login node

This is one of the most important HPC rules.

The login node is generally intended for lightweight tasks such as:

- editing files
- compiling small programs
- inspecting files
- submitting jobs
- managing environments

Don't run a long-running or computationally intensive program directly from the VS Code terminal.

Instead, submit your work to the [Slurm batch scheduler](slurm.md).

## Running interactive jobs

For development, debugging, or testing, an interactive compute session is often more convenient.

For example:

```
srun -p PARTITION -A ACCOUNT --pty --cpus-per-task=4 --mem=8G --time=01:00:00 bash
```

Once the job starts, your VS Code shell is running on a compute node rather than the login node.

You can then run your program:

python my_script.py

This is particularly useful when you need access to GPUs or other compute-node resources.

## Using VS Code for debugging

VS Code can be especially useful for debugging Python or other languages remotely.

A typical workflow is:

Local computer -> SSH -> Login node -> Jub submission -> Compute node -> Your job

For straightforward development, you can edit the code through VS Code and use the terminal to submit jobs.

For more advanced workflows, VS Code can also attach to an interactive compute node, allowing you to use features such as the debugger, Python interpreter, Jupyter notebooks, and language servers on the compute node.

## Prevent VS Code from scanning large HPC filesystems

You should avoid allowing VS Code to index or search entire filesystems such as /snap*, /cosma*,  since recursive scanning can generate a large amount of filesystem traffic and may negatively affect both your session and the system.

VS Code provides settings that let you exclude directories from file watching, searching, and Explorer operations.

For example, add the following to your VS Code settings.json:

```
{
    "files.watcherExclude": {
        "**/.git/**": true,
        "**/cosma/**": true,
        "**/cosma8/**": true,
        "**/cosma7/**": true,
        "**/cosma7/**": true,
        "**/cosma6/**": true,
        "**/cosma5/**": true,
        "**/snap8/**": true,
        "**/snap7/**": true,
    },

    "search.exclude": {
        "**/.git/**": true,
        "**/cosma/**": true,
        "**/cosma8/**": true,
        "**/cosma7/**": true,
        "**/cosma7/**": true,
        "**/cosma6/**": true,
        "**/cosma5/**": true,
        "**/snap8/**": true,
        "**/snap7/**": true,
    },

    "files.exclude": {
        "**/.git/**": true,
        "**/cosma/**": true,
        "**/cosma8/**": true,
        "**/cosma7/**": true,
        "**/cosma7/**": true,
        "**/cosma6/**": true,
        "**/cosma5/**": true,
        "**/snap8/**": true,
        "**/snap7/**": true,
    }
}

You can also add your own directories, for example if you have a large data directory, you can exclude that.

### Excluding HPC-wide filesystems

Be particularly careful if you have opened a high-level directory such as:

```
/cosma/home/PROJECT/your_username
```

If these contain many projects, datasets, or millions of files, don't open the whole directory in VS Code. Instead, open the specific project:

````
/cosma/home/PROJECT/your_username/project_a
```

This is usually preferable to trying to exclude everything else after opening a huge filesystem hierarchy.

### Git repositories

For large repositories, .git directories should normally be excluded from file watching and searching:

```
{
    "files.watcherExclude": {
        "**/.git/**": true
    }
}
```

VS Code and Git can otherwise generate substantial filesystem activity in large repositories.

### Extensions can also scan files

The VS Code core isn't the only source of filesystem activity. Extensions such as Python, C/C++, language servers, linters, Git tools, and notebook extensions may scan files independently.  Please consider:

- installing only extensions you actually need;
- excluding large data/output directories;
- avoiding opening your entire home or project hierarchy;
- keeping datasets and generated output outside the source tree where practical;
- checking extension-specific settings if an extension is still scanning files.

### A good HPC principle

Only open the smallest directory that contains the code you are currently working on.

For example, prefer:

/cosma/home/project/username/src/my_project

over:

/cosma/home/project/username

This reduces unnecessary filesystem operations and makes VS Code considerably more responsive.

Also, don't assume that files.watcherExclude prevents every form of scanning. It primarily controls file watching; search, language servers, Git, and individual extensions can have separate mechanisms and settings.

