""" darkbox template for a command """

import argparse
import hashlib
import sys

class sha256sum:
    def __init__(self):
        self.version = '0.0.0'
    
    def get_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("files", nargs="*")
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

        for i in args["files"]:
            try:
                with open(i, 'r') as f:
                    hash_ret = hashlib.new("sha256", f.read().encode("utf-8"))
                print("{} {}".format(hash_ret.hexdigest(), i))

            except IsADirectoryError:
                print("{}: {}: Is a directory".format(self.__class__.__name__, i), file=sys.stderr)
