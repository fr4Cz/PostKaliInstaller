#!/usr/bin/env python3
#
#   This config file should only contain a comma separated list of scripts to run.
#   Note any scripts in this list will be executed in the beginning of the installation
#   This will allow scripts for adding repositories etc to be run in advance of e.g. apt
#
#   Shell scripts can be places anywhere, however it is a good idea to place them in the <PKI_ROOT>/packages/config.
#
cfg = [
    '{}/add_user.sh',
]
