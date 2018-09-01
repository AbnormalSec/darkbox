"""darkbox sha384sum command"""

from .sha256sum import sha256sum


class sha384sum(sha256sum):
    """darkbox sha384sum

    compute and check SHA384 message digest

    Designed to be similar to sha384sum from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/sha384sum
    """

    def __init__(self):
        super().__init__()
        self.algo = 'sha384'
