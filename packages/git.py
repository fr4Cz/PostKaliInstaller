#!/usr/bin/env python3
#
#   This config file should only contain a dictionary with content to clone from a git repository.
#   Note that any file pulled will be placed under the git/<name> directory.
#   Any project needing additional configuration or setup procedures can have a separate shell script associated.
#   Shell scripts can be places anywhere, however it is a good idea to place them in the packages/config.
#
#   Valid Configuration Syntax:
#   cfg = {
#       "name": {
#           "url": "<url_to_git_project>",
#            "config": "<path_to_shell_script>"
#       }
#   }
#
cfg = {
    "tools": {
        "unicorn": {
            "url": "https://github.com/trustedsec/unicorn.git",
            "config": ""
        },
        "shellKiller": {
            "url": "https://github.com/0x00-0x00/Shellkiller.git",
            "config": ""
        },
        "sn1per": {
            "url": "https://github.com/1N3/Sn1per.git",
            "config": ""
        },
        "apt2": {
            "url": "https://github.com/MooseDojo/apt2.git",
            "config": ""
        },
        "ivre": {
            "url": "https://github.com/cea-sec/ivre.git",
            "config": ""
        },
        "lolbas": {
            "url": "https://github.com/LOLBAS-Project/LOLBAS.git",
            "config": ""
        },
        "pspy": {
            "url": "https://github.com/DominicBreuker/pspy.git",
            "config": ""
        },
        "pupy": {
            "url": "https://github.com/n1nj4sec/pupy.git",
            "config": ""
        },
        "rsg": {
            "url": "https://github.com/mthbernardes/rsg.git",
            "config": ""
        },
        "duckencoder": {
            "url": "https://github.com/mame82/duckencoder.py.git",
            "config": ""
        },
        "empire": {
            "url": "https://github.com/EmpireProject/Empire.git",
            "config": ""
        },
        "psinject": {
            "url": "https://github.com/EmpireProject/PSInject.git",
            "config": ""
        },
        "ptf": {
            "url": "https://github.com/trustedsec/ptf.git",
            "config": ""
        }
    },

    "dictionaries": [
        "https://github.com/danielmiessler/SecLists.git",
    ],

    "other": [
        "https://github.com/chubin/cheat.sh.git",
        "https://github.com/vitalysim/Awesome-Hacking-Resources.git"
    ]
}