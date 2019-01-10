#!/usr/bin/env bash
#
#   Adds a new user to the system.
#   Remember that it is never a good idea to run as root.
#
/usr/bin/mkdir -p /home/${PKIUSR} 2>> ${PKILOG}
/usr/sbin/useradd -u ${PKIUID} -g staff -d /home/${PKIUSR} -s /bin/bash -p $(/usr/bin/echo ${PKIPSW} | /usr/bin/openssl passwd -1 -stdin) ${PKIUSR} 2>> ${PKILOG}
/usr/bin/chown -R -f ${PKIUSR}:staff /home/${PKIUSR} 2>> ${PKILOG}
/usr/bin/chmod 755 /home/${PKIUSR} 2>> ${PKILOG}
/usr/bin/usermod -a -G sudo ${PKIUSR}
/usr/bin/echo "INFO: Added new user with username: ${PKIUSR} and password: ${PKIPSW}, REMEMBER TO CHANGE THE PASSWORD BEFORE USING THE SYSTEM!" >> ${PKILOG}