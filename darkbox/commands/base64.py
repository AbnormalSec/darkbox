"""darkbox base64 command"""

import os
import argparse

from textwrap import wrap
from base64 import b64encode, b64decode
from darkbox.commands.template import Command


class base64(Command):
    """darkbox base64

    base64 encode/decode data and print to standard output

    Designed to be similar to base64 from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/base64
    """

    def __init__(self):
        self.version = '0.1.0'

    def get_parser(self):
        parser = super().get_parser(description='darkbox base64')
        parser.add_argument('file', help='input file')
        parser.add_argument('-d', '--decode', action='store_true', help='decodes input')
        parser.add_argument('-w', '--wrap', type=int, default=76)
        return parser

    def run(self, args=None):
        args = self.get_args(args)
        file_path = args['file']

        try:
            with open(file_path, 'rb') as f:
                in_data = f.read()
        except FileNotFoundError:
            self.file_not_found_error(file_path)
            return
        except IsADirectoryError:
            self.directory_error(file_path)
            return

        if args['decode']:
            in_data = in_data.replace(b'\n', b'')
            print(b64decode(in_data).decode('utf-8'), end='')
        else:
            print('\n'.join(wrap(b64encode(in_data).decode('utf-8'), args['wrap'])))
