""" darkbox ls command """

from .template import Command

import os
import argparse


class ls(Command):
    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = super().get_parser()
        return parser
    
    def run(self):
        args = self.get_args()
        print(' '.join(os.listdir()))
