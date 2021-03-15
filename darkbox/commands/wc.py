"""darkbox wc command"""

from darkbox.commands.template import Command


class wc(Command):
    """darkbox wc

    print newline, word, and byte counts for each file

    Designed to be similar to wc from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/wc
    """

    def __init__(self):
        self.version = '0.1.0'

    def get_parser(self):
        parser = super().get_parser(description='darkbox wc')
        parser.add_argument('-c', '--bytes', action='store_true')
        parser.add_argument('-l', '--lines', action='store_true')
        parser.add_argument('-w', '--words', action='store_true')
        parser.add_argument('files', nargs='+', help='input file')
        return parser

    def run(self, args=None):
        args = self.get_args(args)

        settings = ['lines', 'bytes', 'words']

        # if none are chosen, then choose all (per GNU behavior)
        if not any(args[i] for i in settings):
            for i in settings:
                args[i] = True

        totals = {k:0 for k in settings}

        for i in args['files']:
            try:
                with open(i, 'rb') as f:
                    file_metrics = {k:0 for k in settings}

                    curr_char = f.read(1)
                    while curr_char != b'':
                        file_metrics['bytes'] += 1
                        if curr_char == b'\n': file_metrics['lines'] += 1
                        if curr_char in b'\n\t ': file_metrics['words'] += 1
                        curr_char = f.read(1)

                for k in settings: 
                    totals[k] += file_metrics[k]

                print(f'{file_metrics['lines']} {file_metrics['words']} {file_metrics['bytes']} {i}')

            except FileNotFoundError:
                self.file_not_found_error(i)

            except IsADirectoryError:
                self.directory_error(i)

        if len(args['files']) > 1:
            print(f'{totals["lines"]} {totals["words"]} {totals["bytes"]} total')