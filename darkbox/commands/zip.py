""" darkbox zip command """

from darkbox.commands.template import Command

import os
import zipfile
import argparse


class zip(Command):
    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = super().get_parser('darkbox zip')
        parser.add_argument('zipfile', help='zip file name')
        parser.add_argument('list', help='file list', nargs='*')
        return parser
    
    def run(self):
        args = self.get_args()
        zf = args['zipfile']

        with zipfile.ZipFile(zf, 'w') as myzip:
            for file_path in args['list']:
                if os.path.isfile(file_path):
                    myzip.write(file_path)
                    print("  adding: {}".format(file_path))
                elif os.path.isdir(file_path):
                    for root, dirs, files in os.walk(file_path):
                        for f in files:
                            fp = os.path.join(root, f)
                            myzip.write(fp)
                            print("  adding: {}".format(fp))
                elif not os.path.isfile(file_path):
                    self.file_not_found_error(file_path)
