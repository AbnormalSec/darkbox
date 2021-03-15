"""darkbox mv command"""

import argparse

from shutil import move
from darkbox.commands.template import Command


class mv(Command):
    """darkbox mv

    move (rename) files

    Designed to be similar to mv from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/mv
    """

    def __init__(self):
        self.version = '0.1.0'
    
    def get_parser(self):
        parser = super().get_parser(description='darkbox mv')
        parser.add_argument('src', help='source')
        parser.add_argument('dst', help='destination')
        return parser
    
    def run(self, args=None):
        args = self.get_args(args)
        src = args['src']
        dst = args['dst']
        move(src, dst)
