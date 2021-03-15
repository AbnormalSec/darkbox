"""darkbox yes command"""

from darkbox.commands.template import Command


class yes(Command):
    """darkbox yes

    output a string repeatedly until killed

    Designed to be similar to yes from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/yes
    """

    def __init__(self):
        self.version = '0.1.0'

    def get_parser(self):
        parser = super().get_parser(description='darkbox yes')
        parser.add_argument(
            'string', nargs='*', default='y', help='string to output'
        )
        return parser

    def run(self, args=None):
        args = self.get_args(args)

        out_string = ' '.join(args['string'])
        while True:
            print(out_string)
