"""darkbox factor command"""

from sys import stderr
from darkbox.commands.template import Command


class factor(Command):
    """darkbox factor

    prints prime factors

    Designed to be similar to factor from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/factor
    """

    def __init__(self):
        self.version = '0.1.0'

    def get_parser(self):
        parser = super().get_parser(description='darkbox factor')
        parser.add_argument('numbers', nargs='+', help='integers')
        return parser

    def run(self, args=None):
        args = self.get_args(args)
        
        for i in args['numbers']:
            try:
                num = int(i)

                print(f'{num}:', end='')

                while not (num & 1) and num != 0:
                    print(' 2', end='')
                    num >>=1

                f = 3
                while num > 1:
                    while (num % f) == 0:
                        print(f' {f}', end='')
                        num /= f
                    f+=2

                print() # just for the newline

            except ValueError:
                print(f'factor: '{i}' is not a valid positive integer', file=stderr)
