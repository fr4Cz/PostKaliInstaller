#!/usr/bin/env bash
#
#   Adds a new user to the system.
#   Remember that it is never a good idea to run as root.
#
USR="user"
PSW="Kali"

/usr/bin/mkdir -p /home/${USR}
/usr/sbin/useradd -u 20001 -g users -d /home/${USR} -s /bin/bash -p $(/usr/bin/echo ${PSW} | /usr/bin/openssl passwd -1 -stdin) ${USR}
/usr/bin/chown -R -f ${USR}:users /home/${USR}
/usr/bin/chmod 664 /home/${USR}
/usr/bin/echo "INFO: Added new user with username: ${USR} and password: ${PSW}, REMEMBER TO CHANGE THE PASSWORD BEFORE USING THE SYSTEM!" >> pk_install.log