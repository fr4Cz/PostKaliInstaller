
# Post Kali Installer
This script was built for simple post installation of any tool needed
after the initial installation of the regular 64 bit version of Kali Linux.

For configuring this script according to your own needs please review
the configuration files in the packages directory and change them according to your preferred configuration.

Please note that there are several packages added to the different configurations by default.

## Configuration Arguments
It is possible to run in simulation mode and enable debug mode by passing the
proper arguments to the constructor. The following configuration will enable
debug logging and only run a simulation of the installer.

Note: By running in simulator mode the script will only log the steps it would take.
No files will be added or executed in this mode and should only be used for debugging issues.

    config = {
        'DEBUG': True,
        'SIMULATOR': True
    }

    pki = PKInstall(config)
    pki.install()


## Only Run Selected Tasks
By adding the skip arbument to the constructor configuration it is possible
to skip certain installations e.g. to ommit apt-get and wget installations
the following skip config should be passed:

    config = {
        'skip': {
            'apt': True,
            'wget: True
        }
    }

    pki = PKInstall(config)
    pki.install()


#### Available Installation Sources
The PK Installer will currently give the possibillity to install various
functionality from different sources. The following will be run in the installer
to expand the vanilla Kali Linux installation. Note that adding new repositories should
be done carefully as it might cause Linux to become unstable.

* apt
* git
* wget
* scripts

## Writing Scripts
The installer will run any shell script which is supported by /bin/sh
Please make sure to test any scripts in advance of adding them to the installer,
also remember that it is a bad idea to run random scripts off the internet without a proper review.
