""" darkbox cat command """

import os
import argparse


class cat:
    def __init__(self):
        self.version = '0.0.1'
    
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
        
        if not args['files']:
            print(parser.print_help())
            return

        for i in args["files"]:
            if os.path.isdir(i):
                    print("{cls}: {f}: Is a directory".format(
                        cls=self.__class__.__name__,
                        f=i
                    ))
                    continue
            if not os.path.isfile(i):
                print("{cls}: {f}: No such file or directory".format(
                    cls=self.__class__.__name__,
                    f=i
                ))
                continue

            with open(i, 'r') as f:
                for line in f:
                    print(line, end="")
