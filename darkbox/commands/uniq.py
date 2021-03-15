"""darkbox uniq command"""

from darkbox.commands.template import Command


class uniq(Command):
    """darkbox uniq

    report or omit repeated lines

    Designed to be similar to uniq from GNU coreutils.
    Resource: https://www.gnu.org/software/coreutils/uniq
    """

    def __init__(self):
        self.version = '0.1.0'

    def get_parser(self):
        parser = super().get_parser(description='darkbox uniq')
        parser.add_argument(
            'file',
            help='input file'
        )
        parser.add_argument(
            '-c', '--count', action='store_const', const='{cnt} {str}', default='{str}',
            help='prefix lines by the number of occurrences')
        parser.add_argument(
            '-d', '--repeated', action='store_true',
            help='only print duplicate lines'
        )
        parser.add_argument(
            '-i', '--ignore-case', action='store_const', const=str.lower, default=str,
            help='ignore differences in case when comparing'
        )
        parser.add_argument(
            '-u', '--unique', action='store_true',
            help='only print unique lines'
        )
        # parser.add_argument('-z', '--zero-terminated', action='store_true',
        #                     help='end lines with 0 byte, not newline')
        return parser

    def run(self, args=None):
        args = self.get_args(args)
    
        fmtstr = args['count']
        compare = args['ignore_case']
    
        try:
            with open(args['file'], 'r') as f:
                old_line = f.readline()
                count = 1
                for line in f:
                    if compare(line) != compare(old_line):
                        if not (count == 1 and args['repeated']):
                            if not (count > 1 and args['unique']):
                                print(fmtstr.format(cnt=count, str=old_line), end='')
                        count = 1
                        old_line = line
                    else:
                        count += 1

            if not (count == 1 and args['repeated']):
                if not (count > 1 and args['unique']):
                    print(fmtstr.format(cnt=count, str=old_line), end='')
                
        except FileNotFoundError:
            self.file_not_found_error(args['file'])

        except IsADirectoryError:
            self.directory_error(args['file'])