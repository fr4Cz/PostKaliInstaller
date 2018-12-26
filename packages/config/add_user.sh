#!/usr/bin/env bash
#
#   Adds a new user to the system.
#   Remember that it is never a good idea to run as root.
#
USR="user"
PSW="Kali"

useradd -u 20001 -g users -d /home/${USR} -s /bin/bash -p $(echo ${PSW} | openssl passwd -1 -stdin) ${USR}
echo "INFO: Added new user with username: ${USR} and password: ${PSW}, REMEMBER TO CHANGE THE PASSWORD BEFORE USING THE SYSTEM!" >> ../../pk_install.log
