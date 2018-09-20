"""darkbox false command"""

from darkbox.commands.template import Command


class false(Command):
    """darkbox false

    do nothing and return false

    Designed to be similar to false from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/false
    """

    def __init__(self):
        self.version = '0.0.1'
    
    def run(self, args=None):
        exit(1) 
