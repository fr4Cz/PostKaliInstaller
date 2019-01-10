#!/usr/bin/env bash
#
#   Installs Atom package fetched with WGET
#
/usr/bin/dpkg -i ${PKIROOT}/tools/deb 2>> ${PKILOG}
/usr/bin/rm ${PKIROOT}/tools/deb 2>> ${PKILOG}