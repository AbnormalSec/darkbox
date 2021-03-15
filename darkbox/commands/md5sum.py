"""darkbox md5sum command"""

from .sha256sum import sha256sum


class md5sum(sha256sum):
    """darkbox md5sum

    compute and check MD5 message digest

    Designed to be similar to md5sum from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/md5sum
    """

    def __init__(self):
        super().__init__()
        self.algo = 'md5'
