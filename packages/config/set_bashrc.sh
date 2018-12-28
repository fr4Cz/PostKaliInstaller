#!/usr/bin/env bash
#
#   This script builds a very basic .bashrc file in the home directory of the user running it.
#
_BRC="${PKIROOT}/bashrc.tmp"

/usr/bin/echo "# Prompt" >> ${_BRC}
/usr/bin/echo "export PS1=\"\\[\\033[38;5;10m\\]\\u\\[\$(tput sgr0)\\]\\[\\033[38;5;15m\\] \\[\$(tput sgr0)\\]\\[\\033[38;5;11m\\]@\\[\$(tput sgr0)\\]\\[\\033[38;5;15m\\] \\[\$(tput sgr0)\\]\\[\\033[38;5;39m\\]\\h\\[\$(tput sgr0)\\]\\[\\033[38;5;15m\\] \\w \\[\$(tput sgr0)\\]\\[\\033[38;5;39m\\]\\\\$:\\[\$(tput sgr0)\\]\\[\\033[38;5;15m\\] \\[\$(tput sgr0)\\]\"" >> $_BRC
/usr/bin/echo "export SUDO_PS1=\"\\[\\033[38;5;9m\\]\\u\\[\$(tput sgr0)\\]\\[\\033[38;5;15m\\] \\[\$(tput sgr0)\\]\\[\\033[38;5;11m\\]@\\[\$(tput sgr0)\\]\\[\\033[38;5;15m\\] \\[\$(tput sgr0)\\]\\[\\033[38;5;39m\\]\\h\\[\$(tput sgr0)\\]\\[\\033[38;5;15m\\] \\w \\[\$(tput sgr0)\\]\\[\\033[38;5;9m\\]\\\\$:\\[\$(tput sgr0)\\]\\[\\033[38;5;15m\\] \\[\$(tput sgr0)\\]\"" >> $_BRC

/usr/bin/echo "# Colors" >> ${_BRC}
/usr/bin/echo "export CLICOLOR=1" >> ${_BRC}
/usr/bin/echo "export LSCOLORS=GxFxCxDxBxegedabagaced" >> ${_BRC}

/usr/bin/echo "# Aliases" >> ${_BRC}
/usr/bin/echo "alias ls='/usr/bin/ls --color=auto'" >> ${_BRC}
/usr/bin/echo "alias la='/usr/bin/ls -lah'" >> ${_BRC}
/usr/bin/echo "alias ll='/usr/bin/ls -lh'" >> ${_BRC}
/usr/bin/echo "alias tree='tree -C'" >> ${_BRC}

/usr/bin/cp ${_BRC} /home/${PKIUSR}/.bashrc 2>> ${PKILOG}
/usr/bin/chown -f ${PKIUSR}:staff /home/${PKIUSR}/.bashrc 2>> ${PKILOG}
/usr/bin/rm ${_BRC}