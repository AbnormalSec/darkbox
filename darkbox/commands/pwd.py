"""darkbox pwd command"""

from darkbox.commands.template import Command

import os
import argparse


class pwd(Command):
    """darkbox pwd

    print name of current/working directory

    Designed to be similar to pwd from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/pwd
    """

    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = super().get_parser(description='darkbox pwd')
        return parser
    
    def run(self, args=None):
        args = self.get_args(args)
        print(os.getcwd())
