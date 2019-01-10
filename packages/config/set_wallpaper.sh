#!/usr/bin/env bash
#
#   This script changes the default Kali desktop and lock-screen
#
_IMG="file://${PKIPKGROOT}/wp.png"
/usr/bin/gsettings set org.gnome.desktop.background picture-uri ${_IMG}
/usr/bin/gsettings set org.gnome.desktop.screensaver picture-uri ${_IMG}