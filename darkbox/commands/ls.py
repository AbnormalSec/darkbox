"""darkbox ls command"""

from darkbox.commands.template import Command

import os
import argparse


class ls(Command):
    """darkbox ls

    list directory contents

    Designed to be similar to ls from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/ls
    """

    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = super().get_parser(description='darkbox ls')
        return parser
    
    def run(self):
        args = self.get_args()
        print(' '.join(os.listdir()))
