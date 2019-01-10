#!/usr/bin/env bash
#
#   Fix all file permissions
#
/usr/bin/chown -R ${PKIUSR}:staff /home/${PKIUSR} 2>> ${PKILOG}