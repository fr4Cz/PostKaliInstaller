#!/usr/bin/env python3
#
#   Post Kali Installer
#   --------------------
#   This script was built for simple post installation of any tool needed
#   after the initial installation of the regular 64 bit version of Kali Linux.
#
#   For configuring this script according to your own needs please review the packages in the
#   _apt_packages() and _git_packages() functions and change them according to your preferred configuration.
#   If you are new to Kali Linux then you should be ok running the vanilla configuration.
#
#
#   Author: Zorko
#   Year:   2018
#   Contact: contact@zorko.co
#   Website: www.zorko.co
#
import os
import sys
import logging
import datetime as dt
from subprocess import STDOUT, check_call


class PKInstall:
    __DEBUG__ = False
    __SOURCES__ = {
        'apt': True,
        'git': True,
        'wget': True
    }

    __GIT__ = ''
    __TOOLS__ = ''

    def __init__(self, args={}):
        # Set default values
        self.__ROOT_PATH__ = os.getcwd()
        self.__ACCESS_RIGHTS__ = 0o755

        self.__SOURCES__['apt'] = True
        self.__SOURCES__['git'] = True
        self.__SOURCES__['wget'] = True

        #
        # Set tools root directory
        if 'root' in args:
            self.__ROOT_PATH__ = args['root'].strip('/')

        self.__GIT__ = '{}/git/'.format(self.__ROOT_PATH__)
        self.__TOOLS__ = '{}/tools/'.format(self.__ROOT_PATH__)

        if self.__ROOT_PATH__ != os.getcwd():
            os.chdir(self.__ROOT_PATH__)

        #
        # Set log-level
        if 'DEBUG' in args:
            self.__DEBUG__ = True
            log_level = logging.DEBUG
        else:
            log_level = logging.INFO

        logging.basicConfig(filename='{}/pk_install.log'.format(self.__ROOT_PATH__), level=log_level)
        logging.info('Started running PK Installer at {}'.format(dt.datetime.now()))
        if 'skip' in args:
            if 'apt' in args['skip']:
                if args['skip']['apt']:
                    self.__SOURCES__['apt'] = False

            if 'git' in args['skip']:
                if args['skip']['git']:
                    self.__SOURCES__['git'] = False

            if 'wget' in args['skip']:
                if args['skip']['wget']:
                    self.__SOURCES__['wget'] = False

        #
        # Set directory rights
        if 'access_rights' in args:
            print('args access_rights:', type(args['access_rights']))
            self.__ACCESS_RIGHTS__ = args['access_rights']

        if self.__DEBUG__:
            msg = "\n\tROOT PATH: {},\n\t" \
                  "ACCESS RIGHTS: {},\n\t" \
                  "INSTALL SOURCES: \n\t\t" \
                  "apt: {},\n\t\t" \
                  "git: {},\n\t\t" \
                  "wget: {},\n\t\t" \
                  "LOG LEVEL: {}".format(self.__ROOT_PATH__,
                                         self.__ACCESS_RIGHTS__,
                                         self.__SOURCES__['apt'],
                                         self.__SOURCES__['git'],
                                         self.__SOURCES__['wget'],
                                         log_level)
            logging.debug(msg)

    def install(self):
        # Prepare directory structure
        # Defaults to: ~/git/ and ~/tools/
        logging.debug('Attempting to build the directory structure')
        self.__build_dir_tree()

        if self.__SOURCES__['apt']:
            logging.debug("Attempting to install packages with apt")
            self.__apt_install()

        if self.__SOURCES__['git']:
            logging.debug("Attempting to install packages with git")
            self.__git_install()

        if self.__SOURCES__['wget']:
            logging.debug("Attempting to install packages with wget")
            self.__wget_install()

        return

    def __build_dir_tree(self):
        logging.debug("Entered self.__build_dir_tree()")

        if os.path.isdir(self.__ROOT_PATH__) and os.access(self.__ROOT_PATH__, os.W_OK):
            try:
                logging.debug("Creating git directory: {}".format(self.__GIT__))
                if not os.path.isdir(self.__GIT__):
                    if self.__SOURCES__['git']:
                        os.mkdir(self.__GIT__, self.__ACCESS_RIGHTS__)
                else:
                    logging.warning('The directory: {} already exists, using existing directory'.format(self.__GIT__))

                logging.debug("Creating tools directory: {}".format(self.__TOOLS__))
                if not os.path.isdir(self.__TOOLS__):
                    if self.__SOURCES__['wget']:
                        os.mkdir(self.__TOOLS__, self.__ACCESS_RIGHTS__)
                else:
                    logging.warning('The directory: {} already exists, using existing directory'.format(self.__TOOLS__))
            except OSError as e:
                logging.fatal(e)
                sys.exit(e)
        return

    def __apt_install(self):
        logging.debug('Entered self.__apt_install()')
        if os.geteuid() != 0:
            logging.debug('Installing software with apt should only be done by root, skipping step...')
            return

        try:
            check_call(['apt-get', 'update'], stdout=open(os.devnull, 'wb'), stderr=STDOUT)

            for pkg in self.__apt_packages():
                logging.debug('Installing {} with apt-get'.format(pkg))
                check_call(['apt-get', 'install', '-y', pkg], stdout=open(os.devnull, 'wb'), stderr=STDOUT)
        except OSError as e:
            logging.fatal(e)
            sys.exit(e)

        logging.debug('Apt done.')
        return

    def __git_install(self):
        logging.debug('Entered self.__git_install()')
        os.chdir(self.__GIT__)

        try:
            for pkg in self.__git_packages():
                logging.debug('Installing {} with git'.format(pkg))
                check_call(['git', 'clone', pkg], stdout=open(os.devnull, 'wb'), stderr=STDOUT)
        except OSError as e:
            logging.warning(e)

        os.chdir(self.__ROOT_PATH__)
        logging.debug('Git done.')
        return

    def __wget_install(self):
        logging.debug('Entered self.__wget_install()')
        os.chdir(self.__TOOLS__)
        try:
            for pkg in self.__wget_packages():
                logging.debug('Installing {} with wget'.format(pkg))
                check_call(['wget', pkg], stdout=open(os.devnull, 'wb'), stderr=STDOUT)
        except OSError as e:
            logging.warning(e)

        os.chdir(self.__ROOT_PATH__)
        logging.debug('Wget done.')
        return

    @staticmethod
    def __apt_packages():
        logging.debug('Entered self.__apt_packages()')

        return [
            'terminator'
        ]

    @staticmethod
    def __git_packages():
        logging.debug('Entered self.__git_packages()')

        return [
            'https://github.com/trustedsec/unicorn.git'
        ]

    @staticmethod
    def __wget_packages():
        return [
            'https://raw.githubusercontent.com/trustedsec/unicorn/master/LICENSE.txt'
        ]


if __name__ == '__main__':
    config = {
        'DEBUG': True,
        'skip': {'apt': True}
    }

    pki = PKInstall(config)
    pki.install()
