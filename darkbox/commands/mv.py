""" darkbox mv command """

from darkbox.commands.template import Command

import argparse

from shutil import move


class mv(Command):
    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = super().get_parser(description='darkbox mv')
        parser.add_argument('src', help='source')
        parser.add_argument('dst', help='destination')
        return parser
    
    def run(self):
        args = self.get_args()
        src = args['src']
        dst = args['dst']
        move(src, dst)
