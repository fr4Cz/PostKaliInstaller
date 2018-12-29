#!/usr/bin/env bash
#
#   Add repositories beyond the standard Kali Linux repo
#

#
# Add TOR
/usr/bin/echo 'deb https://deb.torproject.org/torproject.org stretch main
deb-src https://deb.torproject.org/torproject.org stretch main' > /etc/apt/sources.list.d/tor.list 2>> ${PKILOG}
/usr/bin/wget -O- 'https://pgp.mit.edu/pks/lookup?op=get&search=0xA3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89' | /usr/bin/apt-key add - 2>> ${PKILOG}
