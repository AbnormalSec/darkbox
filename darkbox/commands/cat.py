"""darkbox cat command"""

from darkbox.commands.template import Command


class cat(Command):
    """darkbox cat

    concatenate files and print on the standard output

    Designed to be similar to cat from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/cat
    """

    def __init__(self):
        self.version = '0.1.0'

    def get_parser(self):
        parser = super().get_parser(description='darkbox cat')
        parser.add_argument('files', nargs='+', help='input file')
        return parser

    def run(self, args=None):
        args = self.get_args(args)

        for i in args['files']:
            try:
                with open(i, 'r') as f:
                    for line in f:
                        print(line, end='')

            except FileNotFoundError:
                self.file_not_found_error(i)

            except IsADirectoryError:
                self.directory_error(i)
