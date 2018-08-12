""" darkbox ls command """

import os
import argparse


class ls:
    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-v', '--version',
            default=False, action='store_true')
        return parser
    
    def run(self):
        parser = self.get_parser()
        args = vars(parser.parse_args())
        if args['version']:
            print('darkbox {cls} v{version}'.format(
                cls=self.__class__.__name__,
                version=self.version))
            return
        print(' '.join(os.listdir()))
