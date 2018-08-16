""" darkbox sha384sum command """

from .sha256sum import sha256sum


class sha384sum(sha256sum):
    def __init__(self):
        super().__init__()
        self.algo = 'sha384'
