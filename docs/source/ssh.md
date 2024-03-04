# SSH access

COSMA has 7 login servers:

* COSMA5: login5a, login5b
* COSMA7: login7a, login7b, login7c
* COSMA8: login8a, login8b


To connect to COSMA, you will need to generate a [SSH key pair](/account.md#generating-a-ssh-key),
and upload the public part to SAFE. You should protect your ssh key
with a good passphrase. In addition to this, you will also need to
know your COSMA password, which should obviously be different from
your sshkey passphrase. A single SSH keypair will be able to connect
to all login nodes. Please note that each login node has a separate
fingerprint, which will cause a warning and prompt you to accept it
the first time you try to log in.

The same SSH keypair can also be used for git access (for example, see
[this guide for
GitHub](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)).

If you forget your sshkey passphrase, you will need to generate a new
key and upload it to [SAFE](https://safe.epcc.ed.ac.uk/dirac).

If you forget your COSMA password, you can reset it on [SAFE](https://safe.epcc.ed.ac.uk/dirac).

## Logging in with SSH

If you have done that already, use SSH to connect:

`ssh USER@loginXX.cosma.dur.ac.uk` (where XX is the COSMA you are logging in to)

You may need to specify your ssh key:

`ssh -i /path/to/ssh/key USER@loginXX.cosma.dur.ac.uk`

where `USER` is your COSMA username. This will log you in via a secure
shell to COSMA. You can login to different COSMAs by specifying a
different login node: `login5.cosma.dur.ac.uk` for COSMA5

- `login8.cosma.dur.ac.uk` for COSMA8
- `login7.cosma.dur.ac.uk` for COSMA7
- `login5.cosma.dur.ac.uk` for COSMA5
- etc.

The generic loginX given here will then randomly (round-robin) select
a specific login node (e.g. login7 will put you on one of login7a,
login7b or login7c).

The login systems are also the developing nodes: so they know about
the compilers, have access to modules, and the batch system. Unless
otherwise specified, all of your interactive work should be done on
the login nodes. For instructions on how to submit jobs to the batch
quees, see [slurm](/slurm.md). You can submit jobs to any batch queue
from any login node, and access all the storage from any login node.

You will then be asked to enter your ssh key passphrase (if you run a
key manager, you'll only have to do this once per reboot), and after
that, enter your COSMA password.

If you forget your ssh key passphrase, you will need to generate a new
key and upload it to [SAFE](https://safe.epcc.ed.ac.uk/dirac).

If you forget your COSMA password, you can request a reset on
[SAFE](https://safe.epcc.ed.ac.uk/dirac). In this case, when you log
in, you will need to enter the new password twice (once to log in,
once to begin the password reset process), followed by a new password
of your choice (twice).

To request a password reset on SAFE, select "Login accounts" -> "USER@cosma" and then click the "Request Password Reset" button. A new ssh key can also be uploaded on this page.

## Cannot get access?

If you are receiving permission denied when trying to access COSMA, it
could be:

1. You need to specify your ssh key, e.g. `ssh -i /path/to/ssh/key user@login*.cosma.dur.ac.uk`
2. You need to update your ssh key on [SAFE](https://safe.epcc.ed.ac.uk/dirac)
3. You have forgotten your sshkey passphrase or your COSMA password.

For other reasons, please contact cosma-support.

## Running programmes with graphical interface

If you wish to open a graphical programme on a login node (i.e. to
view a plot in `python`, open a PDF in an `evince` viewer or a
picture in `eog`, view an HDF5 file in `hdfviewer`, etc.), you need to add
-X flag to forward the X server:

`ssh -X USER@login.cosma.dur.ac.uk`

You should then be able to have programmes forwarded to your local X server. For instance, typing

`eog PICTURE.png`

on a COSMA login node will open the file.

This should works out of the box on most Linux / BSD systems. If you
are using macOS, you will need to install XQuartz on your machine.

For many applications, x2go is a better way of getting a graphical
interface. See the [x2go](/x2go.md) pages for more information. It will provide
you with a graphical COSMA desktop. This is more responsive than X11,
and is the recommended way of accessing COSMA graphically.

## Saving SSH Configuration

To save yourself from typing the full command every time, you can save
your SSH configuration in a `~/.ssh/config` file on your local
machine. For instance, if your configuration file looks like this:

    Host cosma
     User USER
     IdentityFile ~/.ssh/id_rsa
     HostName login.cosma.dur.ac.uk
     ForwardX11 yes

typing

`ssh cosma`

will be equivalent to

`ssh -X USER@login.cosma.dur.ac.uk`

To learn about more advanced options, please refer to the manual: `man 5 ssh_config`.

## Reusing SSH connections

To avoid entering passwords too many times, you can multiplex your ssh connection.

To do this, you need to add something like:

```
ControlPath ~/.ssh/controlmasters/%r@%h:%p
ControlMaster auto
ControlPersist yes
```

to your .ssh/config file.

Any new connection will then use the first conneciton.

## Disk Usage

Your home quota is usually 10 GB. The contents of your `$HOME` are
backed up every night, and should only be used for code and small
datasets that are not easily recoverable.

All generated/large datasets should be stored in a separate space,
located in `/cosma[5678]/data/project_name/USER`. Your quota there is
more generous and is currently set by default to 10 TB.

## COSMA8 / COSMA7 / COSMA5 Differences

Due to differences in CPU architecture between COSMA5, 7 and 8,
code compiled with strong optimisation on the COSMA7 login nodes may
not work on the COSMA5 or 8 compute nodes, throwing illegal
instructions errors. Therefore, please try to use COSMA5 login
nodes to compile code for these queues, or add a recompilation step to
your submission script.
