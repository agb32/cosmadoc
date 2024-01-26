# Getting an account

 To get a new COSMA account, you need to apply via the [DiRAC SAFE
 system](https://safe.epcc.ed.ac.uk/dirac/)

 When creating your account, it is essential that you upload an ssh
 key. You should also select the project to which you will belong. This
 @@ -10,11 +11,14 @@ COSMA5), please select project hpcicc. Once this form has been
 submitted, you will then have to wait for COSMA staff to create your
 account. You will be notified by email.

 Detailed instructions are available below.

 You will need an ssh key.

 ## Generating a SSH key

 Authentication requires an SSH key pair. A key pair has two parts:

 @@ -26,8 +30,12 @@ use the public key to generate a "challenge", an encrypted
 message. Only the private key can decode this. Your computer then
 sends the correct response to COSMA, and access is then granted.

 ``ssh-keygen -t ed25519 -C "unique name to identify this key."`` (e.g. ``-C cosmaKey``)

 ``ssh-keygen -t rsa -b 4096``

 On Windows, please follow these instructions.
 @@ -56,56 +64,72 @@ e.g. mira.dur.ac.uk, hamilton.dur.ac.uk, github, etc, provided the
 private part remains on your system.  Take great care with the private
 part. 

 ## SSH from Android

 On Android, use e.g. JuiceSSH. You will need to generate a key pair on
 the app.

 ## SSH on Windows

 Windows 10 and 11 include the ssh-keygen utility, so keys can be
 generated as [here](files/COSMAWindows10sshDocumentation.pdf).  However, if not using WSL, a tool such as Putty
 will be required.

 ![SSH Windows](images/sshwin.png)

 ## Accessing Cosma

 First, you need a SAFE account,

 - (Service Administration From EPCC)
 - Used for all DiRAC facilities.
 - In summary: 
   - `https://safe.epcc.ed.ac.uk/dirac/ <https://safe.epcc.ed.ac.uk/dirac/>`_
   - Create an account (institutional email, not personal email)
   - Upload an ssh key
   - Select your project
     e.g. hpcicc or dpXXX (ask your supervisor)
   - Select COSMA (not COSMOS)
   - Wait...

 ![Creating an Account](images/account1.png)

 ![Creating an Account](images/account2.png)

 ![Creating an Account](images/account3.png)

 ![Creating an Account](images/account4.png)

 ![Creating an Account](images/account5.png)

 ![Creating an Account](images/account6.png)

 ![Creating an Account](images/account7.png)

 ![Creating an Account](images/account8.png)

 ![Creating an Account](images/account9.png)

 ![Creating an Account](images/account10.png)

   - While the account is first authorised...
   - And then created...
   - Finally, you will receive an email!

 ![Creating an Account](images/account11.png)
