""" darkbox hostname command """

from darkbox.commands.template import Command

import socket
import argparse


class hostname(Command):
    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = super().get_parser(description='darkbox hostname')
        parser.add_argument('-s', '--simple', action='store_true',
                            help='trim off any domain information')
        return parser
    
    def run(self):
        args = self.get_args()
        simple = args['simple']
        if simple:
            print(socket.gethostname().split('.')[0])
        else:
            print(socket.gethostname())