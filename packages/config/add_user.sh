#!/usr/bin/env bash
#
#   Adds a new user to the system.
#   Remember that it is never a good idea to run as root.
#
USR="user"
PSW="Kali1234!"

/usr/bin/mkdir -p /home/${USR} 2>> ${PKIROOT}/pk_install.log
/usr/sbin/useradd -u ${PKIUID} -g staff -d /home/${USR} -s /bin/bash -p $(/usr/bin/echo ${PSW} | /usr/bin/openssl passwd -1 -stdin) ${USR} 2>> ${PKIROOT}/pk_install.log
/usr/bin/chown -R -f ${USR}:staff /home/${USR} 2>> ${PKIROOT}/pk_install.log
/usr/bin/chmod 755 /home/${USR} 2>> ${PKIROOT}/pk_install.log
/usr/bin/echo "INFO: Added new user with username: ${USR} and password: ${PSW}, REMEMBER TO CHANGE THE PASSWORD BEFORE USING THE SYSTEM!" >> ${PKIROOT}/pk_install.log