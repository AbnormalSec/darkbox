""" darkbox sha224sum command """

from .sha256sum import sha256sum


class sha224sum(sha256sum):
    def __init__(self):
        super().__init__()
        self.version = '0.0.1'
        self.algo = 'sha224'
