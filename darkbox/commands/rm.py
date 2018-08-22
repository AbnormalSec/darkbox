""" darkbox rm command """

from darkbox.commands.template import Command

import os
import argparse

from shutil import rmtree


class rm(Command):
    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = super().get_parser(description='darkbox rm')
        parser.add_argument('file', help='file')
        parser.add_argument('-r', '--recursive', action='store_true')
        return parser
    
    def run(self):
        args = self.get_args()
        file_path = args['file']
        recursive = args['recursive']

        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path) and recursive:
            rmtree(file_path)
        elif os.path.isdir(file_path) and not recursive:
            self.directory_error(file_path)
        else:
            self.file_not_found_error(file_path)
