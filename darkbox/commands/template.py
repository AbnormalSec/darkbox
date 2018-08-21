""" darkbox template for a command """

import argparse
from sys import stderr


class Command:
    def __init__(self):
        self.version = '0.0.0'
    
    def get_parser(self, description=''):
        parser = argparse.ArgumentParser(description)
        parser.add_argument('-v', '--version',
            action="version",
            version="darkbox {cls} v{ver}".format(
                cls=self.__class__.__name__,
                ver=self.version))
        return parser

    def get_args(self):
        return vars(self.get_parser().parse_args())
    
    def directory_error(self, dir_name):
        print("{cls}: {dir}: Is a directory".format(
                cls=self.__class__.__name__,
                dir=dir_name), file=stderr)

    def file_not_found_error(self, filename):
        print("{cls}: {dir}: No such file or directory".format(
                cls=self.__class__.__name__,
                dir=filename), file=stderr)
    
    # commands that inherit this template should define run()
    # this class will not define it in order to simulate a virtual class
    # the template should not be runnable, but an example is below:

    # def run(self):
    #   args = self.get_args()
    #   ...
