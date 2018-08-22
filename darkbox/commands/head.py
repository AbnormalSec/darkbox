""" darkbox head command """

from darkbox.commands.template import Command


class head(Command):
    def __init__(self):
        self.version = '0.0.1'

    def get_parser(self):
        parser = super().get_parser(description='darkbox head')
        parser.add_argument('file', help='input file')
        parser.add_argument('-n', '--lines', type=int, default=10,
                            help='number of lines to display')
        return parser

    def run(self):
        args = self.get_args()
        file_path = args['file']

        try:
            with open(file_path) as f:
                for line in range(args['lines']):
                    print(f.readline(), end='')
        except FileNotFoundError:
            self.file_not_found_error(file_path)
        except IsADirectoryError:
            self.directory_error(file_path)