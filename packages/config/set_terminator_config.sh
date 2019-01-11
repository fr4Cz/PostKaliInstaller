#!/usr/bin/env bash
#
#   This script fetches and installs the terminator themes plugin and new default configuration for Terminator
#
/usr/bin/pip install requests  2>> ${PKILOG}
/usr/bin/mkdir -p /home/${PKIUSR}/.config/terminator/plugins  2>> ${PKILOG}
/usr/bin/wget https://git.io/v5Zww -O "/home/${PKIUSR}/.config/terminator/plugins/terminator-themes.py"  2>> ${PKILOG}

CFG=/home/${PKIUSR}/.config/terminator/config

/usr/bin/echo "[global_config]" > ${CFG}
/usr/bin/echo "  enabled_plugins = TerminatorThemes, LaunchpadCodeURLHandler, APTURLHandler, LaunchpadBugURLHandler" >> ${CFG}
/usr/bin/echo "  title_inactive_bg_color = \"#dadada\"" >> ${CFG}
/usr/bin/echo "  title_receive_bg_color = \"#dadada\"" >> ${CFG}
/usr/bin/echo "  title_receive_fg_color = \"#000000\"" >> ${CFG}
/usr/bin/echo "  title_transmit_bg_color = \"#dadada\"" >> ${CFG}
/usr/bin/echo "  title_transmit_fg_color = \"#000000\"" >> ${CFG}
/usr/bin/echo "[keybindings]" >> ${CFG}
/usr/bin/echo "[layouts]" >> ${CFG}
/usr/bin/echo "  [[default]]" >> ${CFG}
/usr/bin/echo "    [[[child1]]]" >> ${CFG}
/usr/bin/echo "      parent = window0" >> ${CFG}
/usr/bin/echo "      type = Terminal" >> ${CFG}
/usr/bin/echo "    [[[window0]]]" >> ${CFG}
/usr/bin/echo "      parent = \"\"" >> ${CFG}
/usr/bin/echo "      type = Window" >> ${CFG}
/usr/bin/echo "[plugins]" >> ${CFG}
/usr/bin/echo "[profiles]" >> ${CFG}
/usr/bin/echo "  [[default]]" >> ${CFG}
/usr/bin/echo "    background_color = \"#051519\"" >> ${CFG}
/usr/bin/echo "    background_darkness = 0.77" >> ${CFG}
/usr/bin/echo "    background_type = transparent" >> ${CFG}
/usr/bin/echo "    cursor_color = \"#9e9ecb\"" >> ${CFG}
/usr/bin/echo "    foreground_color = \"#e2d8cd\"" >> ${CFG}
/usr/bin/echo "    palette = \"#333333:#f8818e:#92d3a2:#1a8e63:#8ed0ce:#5e468c:#31658c:#e2d8cd:#3d3d3d:#fb3d66:#6bb48d:#30c85a:#39a7a2:#7e62b3:#6096bf:#e2d8cd\"" >> ${CFG}

/usr/bin/chown -R ${PKIUSR}:staff /home/${PKIUSR}/.config 2>> ${PKILOG}