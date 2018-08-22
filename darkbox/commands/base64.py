""" darkbox base64 command """

from darkbox.commands.template import Command

import os
import argparse

from textwrap import wrap
from base64 import b64encode, b64decode


class base64(Command):
    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = super().get_parser(description='darkbox base64')
        parser.add_argument('file', help='input file')
        parser.add_argument('-d', '--decode', action='store_true',
                            help='decodes input')
        parser.add_argument('-w', '--wrap', type=int, default=76)
        # parser.add_argument('-i', '--ignore-garbage', action='store_true')
        return parser

    def run(self):
        args = self.get_args()
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


