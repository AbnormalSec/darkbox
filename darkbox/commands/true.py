"""darkbox true command"""

from darkbox.commands.template import Command


class true(Command):
    """darkbox true

    do nothing, successfully

    Designed to be similar to true from GNU coreutils.
    resource: https://www.gnu.org/software/coreutils/true
    """

    def __init__(self):
        self.version = '0.0.1'
    
    def run(self, args=None):
        exit(0) 
