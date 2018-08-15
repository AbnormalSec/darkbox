""" darkbox cat command """

from .template import Command


class cat(Command):
    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = super().get_parser()
        parser.add_argument('files', nargs='+')
        return parser

    def run(self):
        args = self.get_args()
        
        for i in args['files']:
            try:
                with open(i, 'r') as f:
                    for line in f:
                        print(line, end='')

            except FileNotFoundError:
                self.file_not_found_error(i)

            except IsADirectoryError:
                self.directory_error(i)
