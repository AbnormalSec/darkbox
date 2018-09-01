"""darkbox sha224sum command"""

from .sha256sum import sha256sum


class sha224sum(sha256sum):
    """darkbox sha224sum

    compute and check SHA224 message digest

    Designed to be similar to sha224sum from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/sha224sum
    """

    def __init__(self):
        super().__init__()
        self.algo = 'sha224'
