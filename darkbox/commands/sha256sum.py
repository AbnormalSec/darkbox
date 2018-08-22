""" darkbox sha256sum command """

from darkbox.commands.template import Command

import hashlib


class sha256sum(Command):
    def __init__(self):
        self.version = '0.0.3'
        self.algo = 'sha256'
    
    def get_parser(self):
        parser = super().get_parser(description=
            'darkbox {}sum'.format(self.algo))
        parser.add_argument('files', nargs='*', help='input file(s)')
        return parser
    
    def run(self):
        args = self.get_args()

        files = args['files']
        if not files:
            self.get_parser().print_help()
            return

        for file_path in files:
            try:
                with open(file_path, 'rb') as f:
                    hash_ret = hashlib.new(self.algo, f.read())
                print('{} {}'.format(hash_ret.hexdigest(), file_path))

            except IsADirectoryError:
                self.directory_error(file_path)

            except FileNotFoundError:
                self.file_not_found_error(file_path)
