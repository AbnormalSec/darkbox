"""darkbox template for a command"""

import argparse

from sys import stderr


class Command:
    def __init__(self):
        self.version = '0.0.0'

    def get_parser(self, description=''):
        parser = argparse.ArgumentParser(description)
        parser.add_argument(
            '-v', '--version', action='version',
            version=f'darkbox {self.__class__.__name__} v{self.version}'
        )
        return parser

    def get_args(self, args=None):
        return vars(self.get_parser().parse_args(args))

    def directory_error(self, dir_name):
        print(
            f'{self.__class__.__name__}: {dir_name}: Is a directory',
            file=stderr
        )

    def file_not_found_error(self, filename):
        print(
            f'{self.__class__.__name__}: {filename}: No such file or directory',
            file=stderr
        )

    # commands that inherit this template should define run()
    # this class will not define it in order to simulate a virtual class
    # the template should not be runnable, but an example is below:

    # def run(self):
    #   args = self.get_args()
    #   ...
