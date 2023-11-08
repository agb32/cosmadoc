# SSH access

COSMA has 7 login servers:

* COSMA5: login5a, login5b
* COSMA7: login7a, login7b, login7c
* COSMA8: login8a, login8b


To connect to COSMA, you will need to generate a [SSH key pair](account.rst#generating-a-ssh-key),
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
