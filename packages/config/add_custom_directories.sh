#!/usr/bin/env bash
#
#   Create directories used in CTF events
#

#
# CTF Directories
/usr/bin/mkdir -p /home/${PKIUSR}/Documents/htb/{vpn,boxes}
/usr/bin/chown -R ${PKIUSR}:staff /home/${PKIUSR}/Documents 2>> ${PKILOG}

