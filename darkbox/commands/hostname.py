"""darkbox hostname command"""

import socket
import argparse

from darkbox.commands.template import Command


class hostname(Command):
    """darkbox hostname

    show or set system host name

    Designed to be similar to hostname from GNU inetutils.
    Resource: https://www.gnu.org/software/inetutils/manual/html_node/hostname-invocation.html
    """

    def __init__(self):
        self.version = '0.1.0'

    def get_parser(self):
        parser = super().get_parser(description='darkbox hostname')
        parser.add_argument(
            '-s', '--short', action='store_true', help='short host name'
        )
        return parser

    def run(self, args=None):
        args = self.get_args(args)
        simple = args['short']
        if simple:
            print(socket.gethostname().split('.')[0])
        else:
            print(socket.gethostname())