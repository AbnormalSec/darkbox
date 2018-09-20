"""darkbox factor command"""

from darkbox.commands.template import Command
from sys import stderr

class factor(Command):
    """darkbox factor

    concatenate files and print on the standard output

    Designed to be similar to factor from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/factor
    """

    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = super().get_parser(description='darkbox factor')
        parser.add_argument('numbers', nargs='+', help='integers')
        return parser

    def run(self, args=None):
        args = self.get_args(args)
        
        for i in args['numbers']:
            try:
                num = int(i)

                print("{}:".format(num), end='')

                while not (num & 1) and num != 0:
                    print(" 2", end='')
                    num >>=1

                f = 3
                while num > 1:
                    while (num % f) == 0:
                        print(" {}".format(f), end='')
                        num /= f
                    f+=2

                print('') # just for the newline

            except ValueError:
                print("factor: \"{}\" is not a valid positive integer".format(i), file=stderr)

