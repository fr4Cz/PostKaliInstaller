#!/usr/bin/env python3
#
#   Post Kali Installer
#   --------------------
#   This script was built for simple post installation of any tool needed
#   after the initial installation of the regular 64 bit version of Kali Linux.
#
#   For configuring this script according to your own needs please review the packages in the
#   _apt_packages(), _git_packages(), __wget_packages() methods and change them according to your preferred
#   configuration. If you are new to Kali Linux then you should be ok running the vanilla configuration.
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
import argparse as ap
import datetime as dt
from subprocess import STDOUT, check_call
from colorama import Fore, Style


class PKInstall:
    __DEBUG__ = False
    __SIMULATOR__ = False
    __ROOT_PATH__ = os.getcwd()
    __PACKAGE_ROOT__ = os.getcwd()
    __ACCESS_RIGHTS__ = 0o755
    __GIT__ = '{}/git'.format(__ROOT_PATH__)
    __TOOLS__ = '{}/tools'.format(__ROOT_PATH__)
    __SOURCES__ = {
        'apt': True,
        'git': True,
        'wget': True,
        'scripts': True
    }

    OK = '[' + Fore.GREEN + '+' + Style.RESET_ALL + ']'
    WARN = '[' + Fore.YELLOW + '!' + Style.RESET_ALL + ']'
    FAIL = '[' + Fore.RED + 'x' + Style.RESET_ALL + ']'
    MENU = '[' + Fore.LIGHTBLUE_EX + '-' + Style.RESET_ALL + ']'

    def __init__(self, args={}):
        #
        # Set tools root directory
        if 'root' in args:
            self.__ROOT_PATH__ = args['root'].rstrip('/')

        self.__GIT__ = '{}/git/'.format(self.__ROOT_PATH__)
        self.__TOOLS__ = '{}/tools/'.format(self.__ROOT_PATH__)

        self.__LOG_FILE__ = '{}/pk_install.log'.format(self.__ROOT_PATH__)

        #
        # Define Environment variables used in external scripts
        os.environ['PKIROOT'] = self.__ROOT_PATH__
        os.environ['PKILOG'] = self.__LOG_FILE__

        # Note, remember to change the password manually before using the system!
        os.environ['PKIUSR'] = 'user'
        os.environ['PKIPSW'] = 'Kali1234!'

        os.environ['PKIUID'] = '20001'
        if 'uid' in args and isinstance(args['uid'], int):
            os.environ['PKIUID'] = args['uid']

        if self.__ROOT_PATH__ != os.getcwd():
            os.chdir(self.__ROOT_PATH__)

        if 'SIMULATOR' in args:
            if args['SIMULATOR']:
                self.__SIMULATOR__ = True
        #
        # Set log-level
        if 'DEBUG' in args:
            if args['DEBUG']:
                self.__DEBUG__ = True
                log_level = logging.DEBUG
            else:
                log_level = logging.INFO
        else:
            log_level = logging.INFO

        logging.basicConfig(format='%(levelname)s: %(asctime)s: %(message)s', filename=self.__LOG_FILE__, level=log_level)
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

            if 'scripts' in args['skip']:
                if args['skip']['scripts']:
                    self.__SOURCES__['scripts'] = False

        #
        # Set directory rights
        if 'access_rights' in args:
            print('args access_rights:', type(args['access_rights']))
            self.__ACCESS_RIGHTS__ = args['access_rights']

        if self.__DEBUG__:
            msg = '\n\tROOT PATH: {},\n\t' \
                  'ACCESS RIGHTS: {},\n\t' \
                  'INSTALL SOURCES: \n\t\t' \
                  'apt: {},\n\t\t' \
                  'git: {},\n\t\t' \
                  'wget: {},\n\t\t' \
                  'scripts: {},\n\t\t' \
                  'SIMULATOR MODE: {}\n\t\t' \
                  'UID: {}\n\t\t' \
                  'LOG LEVEL: {}'.format(self.__ROOT_PATH__,
                                         self.__ACCESS_RIGHTS__,
                                         self.__SOURCES__['apt'],
                                         self.__SOURCES__['git'],
                                         self.__SOURCES__['wget'],
                                         self.__SOURCES__['scripts'],
                                         self.__SIMULATOR__,
                                         os.environ['PKIUID'],
                                         log_level)
            logging.debug(msg)

    def install(self):
        print(self.__banner())
        # Prepare directory structure
        # Defaults to: ~/git/ and ~/tools/
        if self.__SIMULATOR__:
            print(self.MENU, Fore.LIGHTRED_EX + 'SIMULATOR Mode Enabled' + Style.RESET_ALL)
            logging.info('SIMULATOR: Running in simulator mode! '
                         'This will only dump commands which would have been run on the system. '
                         'It is recommended that this mode is run with the DEBUG config flag set for the best output')

        print(self.MENU, Fore.LIGHTBLUE_EX + 'Building directory structure' + Style.RESET_ALL)
        logging.debug('Attempting to build the directory structure')
        self.__build_dir_tree()

        if self.__SOURCES__['scripts']:
            print(self.MENU, Fore.LIGHTBLUE_EX + 'Running initial scripts' + Style.RESET_ALL)
            logging.debug('Attempting to run initial scripts')
            self.__scripts_install()

        if self.__SOURCES__['apt']:
            print(self.MENU, Fore.LIGHTBLUE_EX + 'Installing packages with APT' + Style.RESET_ALL)
            logging.debug('Attempting to install packages with apt')
            self.__apt_install()

        if self.__SOURCES__['git']:
            print(self.MENU, Fore.LIGHTBLUE_EX + 'Fetching packages with GIT' + Style.RESET_ALL)
            logging.debug('Attempting to fetch packages with git')
            self.__git_install()

        if self.__SOURCES__['wget']:
            print(self.MENU, Fore.LIGHTBLUE_EX + 'Fetching packages with WGET' + Style.RESET_ALL)
            logging.debug('Attempting to fetch packages with wget')
            self.__wget_install()

        if self.__SOURCES__['scripts']:
            print(self.MENU, Fore.LIGHTBLUE_EX + 'Running final scripts' + Style.RESET_ALL)
            logging.debug('Attempting to run final scripts')
            self.__scripts_install(False)

        print(self.MENU, Fore.LIGHTBLUE_EX + 'FINISHED ' + Style.RESET_ALL + '🍻')
        logging.info('Installation finished at {}'.format(dt.datetime.now()))
        return

    def __build_dir_tree(self):
        logging.debug('Entered self.__build_dir_tree()')

        if os.path.isdir(self.__ROOT_PATH__) and os.access(self.__ROOT_PATH__, os.W_OK):
            try:
                logging.debug('Creating git directory: {}'.format(self.__GIT__))
                if not os.path.isdir(self.__GIT__):
                    if self.__SOURCES__['git']:
                        if self.__SIMULATOR__:
                            msg = 'SIMULATOR: creating directory: {} ' \
                                  'with the following rights {}'.format(self.__GIT__, self.__ACCESS_RIGHTS__)
                            logging.info(msg)
                        else:
                            print(self.OK ,'\tCreating directory: {}'.format(self.__GIT__))
                            os.mkdir(self.__GIT__, self.__ACCESS_RIGHTS__)
                else:
                    print(self.WARN, '\tThe directory: {} already exist'.format(self.__GIT__))
                    logging.warning('The directory: {} already exists, using existing directory'.format(self.__GIT__))

                if os.path.isdir(self.__GIT__):
                    for path in self.__git_packages():
                        new_dir = '{}{}'.format(self.__GIT__, path)

                        if not os.path.isdir(new_dir):
                            print(self.OK, '\tCreating directory: {}'.format(new_dir))
                            os.mkdir(new_dir, self.__ACCESS_RIGHTS__)
                        else:
                            print(self.WARN , '\tThe directory: {} already exist'.format(new_dir))
                            logging.warning('The directory {} already exists, using existing directory'.format(new_dir))

                logging.debug('Creating tools directory: {}'.format(self.__TOOLS__))
                if not os.path.isdir(self.__TOOLS__):
                    if self.__SOURCES__['wget']:
                        if self.__SIMULATOR__:
                            msg = 'SIMULATOR: creating directory: {} ' \
                                  'with the following rights {}'.format(self.__TOOLS__, self.__ACCESS_RIGHTS__)
                            logging.info(msg)
                        else:
                            print(self.OK, '\tCreating directory: {}'.format(self.__TOOLS__))
                            os.mkdir(self.__TOOLS__, self.__ACCESS_RIGHTS__)
                else:
                    print(self.WARN, '\tThe directory: {} already exist'.format(self.__TOOLS__))
                    logging.warning('The directory: {} already exists, using existing directory'.format(self.__TOOLS__))
            except OSError as e:
                print(self.FAIL, '\t' + e)
                logging.fatal(e)
                sys.exit(e)
        return

    def __apt_install(self):
        logging.debug('Entered self.__apt_install()')
        if os.geteuid() != 0:
            print(self.FAIL, '\tInstalling software with apt should only be done by ' + Fore.LIGHTRED_EX + 'root' + Style.RESET_ALL + ', skipping step...')
            logging.error('Installing software with apt should only be done by root, skipping step...')
            return

        try:
            check_call(['apt-get', 'update'], stdout=open(os.devnull, 'wb'), stderr=STDOUT)

            for pkg in self.__apt_packages():
                print(self.OK, '\tInstalling {}'.format(pkg))
                logging.debug('Installing {} with apt-get'.format(pkg))
                if self.__SIMULATOR__:
                    logging.info('SIMULATOR: running command: apt-get install -y {}'.format(pkg))
                else:
                    check_call(['apt-get', 'install', '-y', pkg], stdout=open(os.devnull, 'wb'), stderr=STDOUT)
        except OSError as e:
            print(self.FAIL, '\tFailed installing {} with apt-get'.format(pkg))
            logging.fatal(e)
            sys.exit(e)

        logging.debug('Apt done.')
        return

    def __git_install(self):
        logging.debug('Entered self.__git_install()')
        if not self.__SIMULATOR__:
            logging.debug('Changing directory to: {}'.format(self.__GIT__))
            os.chdir(self.__GIT__)
            logging.debug('CWD: {}'.format(os.getcwd()))

        try:
            packages = self.__git_packages()
            for key in packages:
                if not self.__SIMULATOR__:
                    os.chdir('{}/{}'.format(os.getcwd(), key))

                for pkg in packages[key]:
                    url = packages[key][pkg]['url']
                    cfg = ''
                    if 'config' in packages[key][pkg]:
                        cfg = '{}/{}'.format(self.__ROOT_PATH__, packages[key][pkg]['config'])

                    if not os.path.isdir('{}/{}'.format(os.getcwd(), pkg)) or self.__SIMULATOR__:
                        print(self.OK, '\tCloning {}'.format(url))
                        logging.debug('Installing {} with git'.format(url))
                        try:
                            if self.__SIMULATOR__:
                                logging.info('SIMULATOR: running command: git clone {} {}'.format(url, pkg))
                            else:
                                check_call(['git', 'clone', url, pkg], stdout=open(os.devnull, 'wb'), stderr=STDOUT)

                            if cfg != '':
                                if self.__SIMULATOR__:
                                    logging.info('SIMULATOR: running command: sh {}'.format(cfg))
                                else:
                                    try:
                                        print(self.OK, '\tConfiguring {}'.format(key))
                                        logging.debug('Running {} config script'.format(pkg))
                                        check_call(['sh', cfg], stdout=open(os.devnull, 'wb'), stderr=STDOUT)
                                    except OSError as e:
                                        print(self.FAIL, '\tFailed configuring {}'.format(key))
                                        logging.error(e)
                        except OSError as e:
                            print(self.FAIL, e)
                            logging.error(e)
                    else:
                        print(self.WARN, '\tThe directory {0}/{1} already exists, skipping resource {1}'.format(os.getcwd(), pkg))
                        logging.warning('The directory {0}/{1} already exists, skipping resource {1}'.format(os.getcwd(), pkg))

                if not self.__SIMULATOR__:
                    logging.debug('Changing directory to: {}'.format(self.__GIT__))
                    os.chdir(self.__GIT__)
                    logging.debug('CWD: {}'.format(os.getcwd()))
        except OSError as e:
            print(self.FAIL, '\t' + e)
            logging.error(e)

        if not self.__SIMULATOR__:
            logging.debug('Changing directory to: {}'.format(self.__ROOT_PATH__))
            os.chdir(self.__ROOT_PATH__)
            logging.debug('CWD: {}'.format(os.getcwd()))
        logging.debug('Git done.')
        return

    def __wget_install(self):
        logging.debug('Entered self.__wget_install()')
        if not self.__SIMULATOR__:
            logging.debug('Changing directory to: {}'.format(self.__TOOLS__))
            os.chdir(self.__TOOLS__)
            logging.debug('CWD: {}'.format(os.getcwd()))

        try:
            for pkg in self.__wget_packages():
                print(self.OK, '\tFetching {}'.format(pkg))
                logging.debug('Installing {} with wget'.format(pkg))
                if self.__SIMULATOR__:
                    logging.info('SIMULATOR: running command: wget {}'.format(pkg))
                else:
                    check_call(['wget', pkg], stdout=open(os.devnull, 'wb'), stderr=STDOUT)
        except OSError as e:
            print(self.FAIL, '\t' + e)
            logging.error(e)

        if not self.__SIMULATOR__:
            logging.debug('Changing directory to: {}'.format(self.__ROOT_PATH__))
            os.chdir(self.__ROOT_PATH__)
            logging.debug('CWD: {}'.format(os.getcwd()))
        logging.debug('Wget done.')
        return

    def __scripts_install(self, initial=True):
        logging.debug('Entered self.__scripts_install()')
        try:
            if initial:
                script = self.__initial_scripts()
            else:
                script = self.__final_scripts()

            for pkg in script:
                if "{}" in pkg:
                    p = pkg.format(self.__PACKAGE_ROOT__ + "/packages/config")
                else:
                    p = pkg

                print(self.OK, '\tRunning {}'.format(p))
                logging.debug('Running {}'.format(p))
                if self.__SIMULATOR__:
                    logging.info('SIMULATOR: running command: sh {}'.format(p))
                else:
                    # TODO; Find a way to redirect stdout from scripts to logger
                    try:
                        if os.path.isfile(p):
                            check_call(['sh', p], stdout=open(os.devnull, 'wb'), stderr=STDOUT, env=dict(os.environ))
                        else:
                            print(self.FAIL, '\t{} does not exist'.format(p))
                            logging.error('{} does not exist'.format(p))
                    except OSError as e:
                        print(self.FAIL, '\t' + e)
                        logging.error(e)
        except OSError as e:
            print(self.FAIL, '\t' + e)
            logging.error(e)

        logging.debug('Scripts done.')
        return

    @staticmethod
    def __initial_scripts():
        logging.debug('Entered self.__initial_scripts()')
        from packages import initial_scripts
        return initial_scripts.cfg

    @staticmethod
    def __final_scripts():
        logging.debug('Entered self.__final_scripts()')
        from packages import final_scripts
        return final_scripts.cfg

    @staticmethod
    def __apt_packages():
        logging.debug('Entered self.__apt_packages()')
        from packages import apt
        return apt.cfg

    @staticmethod
    def __git_packages():
        logging.debug('Entered self.__git_packages()')
        from packages import git
        return git.cfg

    @staticmethod
    def __wget_packages():
        logging.debug('Entered self.__wget_packages()')
        from packages import wget
        return wget.cfg

    @staticmethod
    def __banner():
        return Fore.RED + '''
       ██▓███   ██ ▄█▀ ██▓
      ▓██░  ██▒ ██▄█▒ ▓██▒
      ▓██░ ██▓▒▓███▄░ ▒██▒
      ▒██▄█▓▒ ▒▓██ █▄ ░██░
      ▒██▒ ░  ░▒██▒ █▄░██░
      ▒▓▒░ ░  ░▒ ▒▒ ▓▒░▓  
      ░▒ ░     ░ ░▒ ▒░ ▒ ░
      ░░       ░ ░░ ░  ▒ ░
            ░  ░    ░  
        ''' + Style.RESET_ALL + '''
.+´ Post Kali Installer v1.0 `+.
        '''


def main():
    p = ap.ArgumentParser()

    p.add_argument('-sA', '--skip-apt', default=False, action='store_true', help='Do not install APT packages')
    p.add_argument('-sG', '--skip-git', default=False, action='store_true', help='Do not fetch GIT packages')
    p.add_argument('-sS', '--skip-scripts', default=False, action='store_true', help='Do not run scripts')
    p.add_argument('-sW', '--skip-wget', default=False, action='store_true', help='Do not fetch WGET packages')

    p.add_argument('-D', '--debug', default=False, action='store_true', help='Run in debug mode')
    p.add_argument('-S', '--simulate', default=False, action='store_true', help='Run in simulator mode')

    p.add_argument('-R', '--set-root', type=str, help='Set install root directory, defaults to current working directory')
    p.add_argument('-cU', '--set-config-uid', type=str, help='Set uid for use in config scripts')
    #p.add_argument('-A', '--set-access-rights', type=str, help='Set access rights for created directories')

    try:
        a = p.parse_args()
        config = _build_config(a)

        pki = PKInstall(config)
        pki.install()
    except ValueError as ve:
        sys.exit(ve)
    return


def _build_config(args):
    config = {}
    if args.skip_apt or args.skip_git or args.skip_wget or args.skip_scripts:
        config['skip'] = {}
        if args.skip_apt:
            config['skip']['apt'] = args.skip_apt
        if args.skip_git:
            config['skip']['git'] = args.skip_git
        if args.skip_wget:
            config['skip']['wget'] = args.skip_wget
        if args.skip_scripts:
            config['skip']['scripts'] = args.skip_scripts
    if args.set_root:
        config['root'] = args.set_root
    if args.debug:
        config['DEBUG'] = args.debug
    if args.simulate:
        config['SIMULATOR'] = args.simulate
    if args.set_config_uid:
        config['uid'] = args.set_config_uid
    # if args.set_access_rights:
    #     config['access_rights'] = args.set_access_rights

    return config


if __name__ == '__main__':
    main()
