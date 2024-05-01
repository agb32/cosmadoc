# Generating a SSH key

Authentication requires an SSH key pair. A key pair has two parts:

- A private part (keep this very safe)
- A public part (give this to COSMA/SAFE)

`ssh` uses the public key to generate a "challenge", an encrypted
 message. Only the private key can decode this. Your computer then
 sends the correct response to COSMA, and access is then granted.

## Unix systems

On Linux or a Mac you can generate a key pair using:

``ssh-keygen -t ed25519 -C "unique name to identify this key."`` (e.g. ``-C cosmaKey``)

or, if that fails (e.g. if you have an old client)

``ssh-keygen -t rsa -b 4096 -C cosmaKey``

This will ask for a passphrase: PLEASE use a strong one, as the use of
a user with a weak passphrase was responsible for the hacking of HPC
systems across Europe, China and the USA in 2020. Something like 16
characters would be good (perhaps several words strung together).

It will also ask for a location. You can use the default, or something else, e.g. `~/.ssh/id_rsa_cosma`.

This will create:

- id_ed25519 - the private part.  Keep this safe, and consider where it is backed up to (e.g. don't back it up to the "cloud" if the cloud is an untrusted provider or could be hacked), and don't copy it to other systems.  Also NEVER send it by email anywhere.
- id_ed25519.pub - the public part.  Upload this to SAFE.

## SSH from Android

On Android, use e.g. JuiceSSH. You will need to generate a key pair on
the app.

## SSH on Windows

Windows 10 and 11 include the ssh-keygen utility, so keys can be
generated as [here](files/COSMAWindows10sshDocumentation.pdf).
However, if not using Windows Subsystem for Linux (WSL), a tool such
as Putty will be required.



![SSH Windows](images/sshwin.png)
