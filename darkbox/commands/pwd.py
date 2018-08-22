""" darkbox pwd command """

from darkbox.commands.template import Command

import os
import argparse


class pwd(Command):
    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = super().get_parser(description='darkbox pwd')
        return parser
    
    def run(self):
        args = self.get_args()
        print(os.getcwd())
