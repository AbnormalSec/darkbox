"""darkbox package command"""

import argparse
import subprocess

from darkbox.commands.template import Command
from darkbox.util.osutil import get_platform, get_distro


class package(Command):
    """darkbox package

    cross-platform package installer

    This tool was written by vesche and is unique to the darkbox project.
    """

    def __init__(self):
        self.version = '0.1.0'

    def get_parser(self):
        parser = super().get_parser(description='darkbox package')
        parser.add_argument('command', help='install or uninstall')
        parser.add_argument('package', help='package name')
        return parser

    def run(self, args=None):
        args = self.get_args(args)

        if args['command'] not in ['install', 'uninstall']:
            self.get_parser().print_help()
            return

        command = args['command']
        package = args['package']

        plat = get_platform()
        distro = get_distro()

        if plat == 'mac':
            pkg_install = 'brew install'
            pkg_uninstall = 'brew uninstall'
        elif plat == 'nix':
            # TODO: full path to binaries?
            if distro == 'centos' or distro == 'redhat':
                pkg_install = 'yum -y install'
                pkg_uninstall = 'yum -y remove'
            elif distro == 'fedora':
                pkg_install = 'dnf -y install'
                pkg_uninstall = 'dnf -y remove'
            elif distro == 'debian':
                pkg_install = 'apt-get -y install'
                pkg_uninstall = 'apt-get -y uninstall'
            elif distro == 'arch':
                pkg_install = 'pacman -S'
                pkg_uninstall = 'pacman -R'
            elif distro == 'SuSE':
                pkg_install = 'zypper install'
                pkg_uninstall = 'zypper uninstall'
            else:
                print('Error: Distro not found!')
                return
        else:
            print('Error: platform unsupported!')
            return

        print(f'darkbox package v{self.version} is attempting to {command} {package}...')
        try:
            if command == 'install':
                c = pkg_install.split() + [package]
                subprocess.check_call(c)
            elif command == 'uninstall':
                c = pkg_uninstall.split() + [package]
                subprocess.check_call(c)
        except FileNotFoundError:
            self.file_not_found_error(pkg_install.split()[0])
        except subprocess.CalledProcessError:
            print(f'Error: {package} could not be installed!')