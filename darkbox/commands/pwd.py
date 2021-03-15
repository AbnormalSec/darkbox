"""darkbox pwd command"""

import os
import argparse

from darkbox.commands.template import Command


class pwd(Command):
    """darkbox pwd

    print name of current/working directory

    Designed to be similar to pwd from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/pwd
    """

    def __init__(self):
        self.version = '0.1.0'
    
    def get_parser(self):
        return super().get_parser(description='darkbox pwd')

    def run(self, args=None):
        args = self.get_args(args)
        print(os.getcwd())
