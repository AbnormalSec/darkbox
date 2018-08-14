""" darkbox sha256sum command """

import hashlib
from .command import Command


class sha256sum(Command):
    def __init__(self):
        self.version = '0.0.2'
        self.algo = "sha256"
    
    def get_parser(self):
        parser = super().get_parser()
        parser.add_argument('files', nargs='*')
        return parser
    
    def run(self):
        args = self.get_args()

        for i in args['files']:
            try:
                with open(i, 'rb') as f:
                    hash_ret = hashlib.new(self.algo, f.read())
                print('{} {}'.format(hash_ret.hexdigest(), i))

            except IsADirectoryError:
                self.directory_error(i)

            except FileNotFoundError:
                self.file_not_found_error(i)
