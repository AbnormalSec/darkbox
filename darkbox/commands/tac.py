"""darkbox tac command"""

from darkbox.commands.template import Command


class tac(Command):
    """darkbox tac

    concatenate and print files in reverse

    Designed to be similar to tac from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/tac
    """

    def __init__(self):
        self.version = '0.1.0'
    
    def get_parser(self):
        parser = super().get_parser(description='darkbox tac')
        parser.add_argument('files', nargs='+', help='input file')
        return parser

    def run(self, args=None):
        args = self.get_args(args)
        
        for i in args['files']:
            try:
                with open(i, 'r') as f:
                    for line in f.readlines()[::-1]:
                        print(line, end='')

            except FileNotFoundError:
                self.file_not_found_error(i)

            except IsADirectoryError:
                self.directory_error(i)
