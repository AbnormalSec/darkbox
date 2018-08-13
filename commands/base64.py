""" darkbox template for a command """

import os
import argparse
from base64 import b64encode, b64decode
from textwrap import wrap


class base64:
    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = argparse.ArgumentParser()

        parser.add_argument('-d', '--decode', action='store_true')
        # parser.add_argument('-i', '--ignore-garbage', action='store_true')
        parser.add_argument('-w', '--wrap', type=int, default=76)
        parser.add_argument('-v', '--version', default=False, action='store_true')
        parser.add_argument("file", nargs="?")
        return parser
   
    def run(self):
        parser = self.get_parser()
        args = vars(parser.parse_args())
        if args['version']:
            print('darkbox {cls} v{version}'.format(
                cls=self.__class__.__name__,
                version=self.version))
            return
        
        file_path = args['file']

        if not file_path:
            print(parser.print_help())
            return

        if not os.path.isfile(file_path):
            print("Error: File not found!")
            return

        with open(file_path, 'rb') as f:
            in_data = f.read()

        if args['decode']:
            in_data = in_data.replace(b"\n",b"")
            print(b64decode(in_data).decode("utf-8"), end='')

        else:
            print('\n'.join(wrap(b64encode(in_data).decode("utf-8"), args['wrap'])))


