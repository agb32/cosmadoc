Getting an account
==================

To get a new COSMA account, you need to apply via the `DiRAC SAFE
system <https://safe.epcc.ed.ac.uk/dirac/>`_

When creating your account, it is essential that you upload an ssh
key. You should also select the project to which you will belong. This
will either be a DiRAC project, or if you are a local Durham user (for
COSMA5), please select project hpcicc. Once this form has been
submitted, you will then have to wait for COSMA staff to create your
account. You will be notified by email.

Detailed instructions are available here

You will need an ssh key.

.. _sshkey:

Generating a SSH key
--------------------

Authentication requires an SSH key pair. A key pair has two parts:

* A private part (keep this very safe)
* A public part (give this to COSMA - or anything else)

SSH uses public key cryptography. When you try to connect, COSMA will
use the public key to generate a "challenge", an encrypted
message. Only the private key can decode this. Your computer then
sends the correct response to COSMA, and access is then granted.

On Linux, or a Mac, to generate a key pair, you can use:

``ssh-keygen -t ed25519 -C "unique name to identify this key."`` (e.g. ``-C cosmaKey``)

If that fails (probably you have an old ssh client), you can try:

``ssh-keygen -t rsa -b 4096``

On Windows, please follow these instructions.

This will ask for a passphrase: PLEASE use a strong one, as the use of
a user with a weak passphrase was responsible for the hacking of HPC
systems across Europe, China and the USA in 2020. Something like 16
characters would be good (perhaps several words strung together).

It will also ask for a location. You can use the default, or something else, e.g. ~/.ssh/id_rsa_cosma.

This will create:

* id_rsa - the private part. Keep this safe, and consider where it is backed up to (e.g. don't back it up to the "cloud"), and don't copy it to other systems. Also NEVER send it by email anywhere.
* id_rsa.pub - the public part. Upload this to SAFE.

cosma-support will then add your key to the system (so it might take a
few minutes, depending how busy we are).

To avoid having to enter your passphase every time you ssh to COSMA,
you can use an ssh-agent. e.g. in your local .bashrc file, you can put
something like: eval $(keychain --eval /path/to/id_rsa 2> /dev/null)

Note, you can use the same public key on other systems,
e.g. mira.dur.ac.uk, hamilton.dur.ac.uk, github, etc, provided the
private part remains on your system.  Take great care with the private
part. 

SSH from Android
^^^^^^^^^^^^^^^^

On Android, use e.g. JuiceSSH. You will need to generate a key pair on
the app.

SSH on Windows
^^^^^^^^^^^^^^

Windows 10 and 11 include the ssh-keygen utility, so keys can be
generated as [here](/files/COSMAWindows10sshDocumentation.pdf).  However, if not using WSL, a tool such as Putty
will be required.

![](./images/sshwin.png)

