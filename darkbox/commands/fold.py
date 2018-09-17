""" darkbox fold command """

from .template import Command


class fold(Command):
    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = super().get_parser()
        parser.add_argument('-w', '--width', type=int, default=80, help='use WIDTH columns instead of 80')
        parser.add_argument('files', nargs='+')
        return parser

    def run(self, args=None):
        args = self.get_args(args)
        
        for i in args['files']:
            try:
                with open(i, 'r') as f:
                    for line in f:
                        # dear god solve this. its awful. but functional.
                        for part in [line.rstrip('\n')[n:n+args['width']] for n in range(0, len(line), args['width'])]:
                            print(part)
                        

            except FileNotFoundError:
                self.file_not_found_error(i)

            except IsADirectoryError:
                self.directory_error(i)
