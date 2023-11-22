# Locale errors

If you are getting locale errors when compiling or running code, check your LANG environment variable (```echo $LANG```).  If this is not set, you can do ```export LANG=en_GB.UTF-8``` and try again.

Compilers do not always handle locales very well. If this works remember to do this everytime you login, or add it to your ```.bash_profile```.

