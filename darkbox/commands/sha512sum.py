"""darkbox sha512sum command"""

from .sha256sum import sha256sum


class sha512sum(sha256sum):
    """darkbox sha512sum

    compute and check SHA512 message digest

    Designed to be similar to sha512sum from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/sha512sum
    """

    def __init__(self):
        super().__init__()
        self.algo = 'sha512'
