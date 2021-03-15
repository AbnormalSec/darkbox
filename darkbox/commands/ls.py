"""darkbox ls command"""

import os
import argparse

from darkbox.commands.template import Command


class ls(Command):
    """darkbox ls

    list directory contents

    Designed to be similar to ls from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/ls
    """

    def __init__(self):
        self.version = '0.1.0'

    def get_parser(self):
        return super().get_parser(description='darkbox ls')

    def run(self, args=None):
        args = self.get_args(args)
        print(' '.join(os.listdir()))
