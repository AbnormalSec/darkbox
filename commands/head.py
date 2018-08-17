""" darkbox template for a command """

from .template import Command

class head(Command):
    def __init__(self):
        self.version = '0.0.1'
    

    def get_parser(self, description=''):
        parser = super().get_parser()
        parser.add_argument("-n", "--lines", type=int, default=10)
        parser.add_argument("file")
        return parser


    def run(self):
        args = self.get_args()
        with open(args['file']) as f:
            for line in range(args['lines']):
                print(f.readline(), end='')