#!/usr/bin/env python3
#
#   This config file should only contain a dictionary with content to clone from a git repository.
#   Note that any file pulled will be placed under the git/<name> directory.
#   Any project needing additional configuration or setup procedures can have a separate shell script associated.
#   Shell scripts can be places anywhere, however it is a good idea to place them in the packages/config, paths are relative to
#   the PK_Installer root directory.
#
#   Valid Configuration Syntax:
#   cfg = {
#       "section": {
#           "name": {
#               "url": "<url_to_git_project>",
#               "config": "<path_to_shell_script>"
#           }
#       }
#   }
#
cfg = {
    "tools": {
        "unicorn": {
            "url": "https://github.com/trustedsec/unicorn.git"
        },
        "shellKiller": {
            "url": "https://github.com/0x00-0x00/Shellkiller.git"
        },
        "sn1per": {
            "url": "https://github.com/1N3/Sn1per.git"
        },
        "apt2": {
            "url": "https://github.com/MooseDojo/apt2.git"
        },
        "ivre": {
            "url": "https://github.com/cea-sec/ivre.git"
        },
        "lolbas": {
            "url": "https://github.com/LOLBAS-Project/LOLBAS.git"
        },
        "pspy": {
            "url": "https://github.com/DominicBreuker/pspy.git"
        },
        "pupy": {
            "url": "https://github.com/n1nj4sec/pupy.git"
        },
        "rsg": {
            "url": "https://github.com/mthbernardes/rsg.git"
        },
        "duckencoder": {
            "url": "https://github.com/mame82/duckencoder.py.git"
        },
        "empire": {
            "url": "https://github.com/EmpireProject/Empire.git"
        },
        "psinject": {
            "url": "https://github.com/EmpireProject/PSInject.git"
        },
        "ptf": {
            "url": "https://github.com/trustedsec/ptf.git"
        },
        "mimikatz": {
            "url": "https://github.com/gentilkiwi/mimikatz"
        },
        "nishang": {
            "url": "https://github.com/samratashok/nishang.git"
        },
        "sherlock": {
            "url": "https://github.com/rasta-mouse/Sherlock.git"
        }
    },

    "dictionaries": {
        "seclists": {
            "url": "https://github.com/danielmiessler/SecLists.git",
        }
    },

    "other": {
        "cheat.sh": {
            "url": "https://github.com/chubin/cheat.sh.git"
        },
        "awesome-hacking-resources": {
            "url": "https://github.com/vitalysim/Awesome-Hacking-Resources.git"
        },
        "awesome-pentest-cheat-sheets": {
            "url": "https://github.com/coreb1t/awesome-pentest-cheat-sheets.git"
        }
    }

}