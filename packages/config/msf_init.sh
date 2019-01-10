#!/usr/bin/env bash
#
#   Initiate the Metasploit database connection
#
systemctl start postgresql 2>> ${PKILOG}
msfdb init 2>> ${PKILOG}