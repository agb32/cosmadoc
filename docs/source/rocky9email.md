# Rocky 9 Cluster welcome email

```
Dear all,

COSMA is now exiting maintenance mode, and returning to production.

You should be able to log in, but you will probably notice several
changes.  Please also consider the system as at-risk for the next few
weeks while we iron out any oddities.

Please note that the host keys have changed, so you will be warned about 
this when logging in for the first time.  You should be able to remove the
old entries from your system using something like:

ssh-keygen -R login8.cosma.dur.ac.uk (or other appropriate login node)

The operating system has been upgraded to the latest Rocky 9.4 OS, with a
new Linux kernel (5.14), glibc and system compilers.  Therefore existing
binaries may need recompiling.  We have left many of the old modules in
place, because some may or may not work depending on use case.  If there
is a module that you rely on which is no longer present, you can:

module load old-modules

which will then allow you to module load the required module.

The default version of compilers, Python, etc has been updated.

There is a new Intel OneAPI (compilers, etc) installation, a new GCC and a
new Python.

The old cosma Slurm partition is still down: cosma5 users should submit to
the newer cosma5 partition for now.  We hope that the old cosma partition
will be made available within a couple of months.

The old cosma5 login nodes (login.cosma.dur.ac.uk, login5a and login5b)   
are not yet available.  Please use login5c.cosma.dur.ac.uk instead.

Some of the Mad nodes (cosma*-shm* partitions) are still down, but will be
made available shortly.

The bluefield1 partition is also not yet available.

The cosma8-dine2 partition has been renamed to dine2.

Currently, the maximum runtime for jobs submitted to the cosma8 partitions
is limited to 2 hours, to allow for rapid testing and turn around.  This
will be reverted to 3 days next week.  The other partitions have their
normal runtimes.

The dataweb node is not yet available.

The AMD GPU nodes are not yet available - we are awaiting driver
updates (this also means that the cosma chatbot will run slower than
usual for now).

You may receive spurious email over the next few weeks while we test
things (e.g. quota alerts, etc).

Your /cosma/home/PROJECT/USER has been moved to a new file system, and we
have added a /cosma/apps/PROJECTS/USER directory.

As before, /cosma/home is backed up nightly.  However, /cosma/apps is not,
but has a significantly larger (100GB) quota.  This is therefore an ideal
place for installing software libraries, Python venvs, spack
installations, etc.  We have softlinked several of your hidden directories
to /cosma/apps (e.g. ~/.share, ~/.cache, etc).  Please note, these spaces
are not designed for running batch jobs from: use e.g. /cosma[5,7,8] for
these as appropriate.

For any x2go users, you may find windows are not refreshing.  To resolve
this, within your x2go session, go to the Applications menu, Settings ->
Settings manager.  Select the "Window Manager Tweaks" icon, and within   
this the "Compositor" tab.  Then untick "Enable display compositing".

The /madfs file system has been retired, along with /cosma7old.

Please let us know if you find anything broken, or unexpected behaviour,
and we will do our best to fix it.  However, for issues around code
compilation, module versions etc, please make an initial attempt to
resolve it.

This email is available at
https://cosma.readthedocs.io/en/latest/rocky9email.html

Unfortunately, we have lost xemacs (for now).  However, standard emacs is
still the recommended text editor of choice (though we understand vi may
be a personal choice for some users).

Best wishes,
Alastair, Mark, Peter, Paul and Richard.
```
