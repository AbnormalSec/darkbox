""" darkbox unzip command """

from darkbox.commands.template import Command

import zipfile
import argparse


class unzip(Command):
    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = super().get_parser('darkbox unzip')
        parser.add_argument('file', help='input file')
        return parser
    
    def run(self):
        args = self.get_args()
        file_path = args['file']

        try:
            with zipfile.ZipFile(file_path) as zf:
                zf.extractall('.')
                print('File {} extracted.'.format(file_path))
        except (zipfile.BadZipfile, OSError):
            print('Error: Failed to unzip file.')
        except IsADirectoryError:
            self.directory_error(file_path)
        except FileNotFoundError:
            self.file_not_found_error(file_path)
