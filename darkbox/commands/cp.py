"""darkbox cp command"""

import os
import argparse

from shutil import copy
from darkbox.commands.template import Command


class cp(Command):
    """darkbox cp

    copy files and directories

    Designed to be similar to cp from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/cp
    """

    def __init__(self):
        self.version = '0.1.0'

    def get_parser(self):
        parser = super().get_parser(description='darkbox cp')
        parser.add_argument('src', help='source')
        parser.add_argument('dst', help='destination')
        parser.add_argument('-r', '--recursive', action='store_true')
        return parser

    def run(self, args=None):
        args = self.get_args(args)
        src = args['src']
        dst = args['dst']
        recursive = args['recursive']
        src_is_dir = False

        if not os.path.exists(src):
            self.file_not_found_error(src)
            return
        if os.path.isdir(src) and not recursive:
            print(f'cp: {src} is a directory (not copied).')
            return

        src_paths = list()
        if os.path.isfile(src):
            src_paths.append(src)
        elif os.path.isdir(src):
            src_is_dir = True
            for root, dirs, files in os.walk(src):
                for f in files:
                    fp = os.path.join(root, f)
                    src_paths.append(fp)

        if src_is_dir and not os.path.exists(dst):
            os.makedirs(dst)

        try:
            for s in src_paths:
                copy(s, dst)
        except FileNotFoundError:
            self.file_not_found_error(dst)
