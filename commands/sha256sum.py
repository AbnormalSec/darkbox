""" darkbox template for a command """

import hashlib
from .template import Command

class sha256sum(Command):
    def __init__(self):
        self.version = '0.0.2'
        self.algo = "sha256"
    
    def get_parser(self):
        parser = super().get_parser()
        parser.add_argument("files", nargs="*")
        return parser
    
    def run(self):
        args = self.get_args()

        for i in args["files"]:
            try:
                with open(i, 'r') as f:
                    hash_ret = hashlib.new(self.algo, f.read().encode("utf-8"))
                print("{} {}".format(hash_ret.hexdigest(), i))

            except IsADirectoryError:
                self.directory_error(i)

            except FileNotFoundError:
                self.file_not_found_error(i)
