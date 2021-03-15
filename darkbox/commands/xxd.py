"""darkbox xxd command"""

import os
import binascii

from darkbox.commands.template import Command


class xxd(Command):
    """darkbox xxd

    make a hexdump or do the reverse

    Designed to be similar to xxd by Juergen Weigert.
    Resource: https://github.com/vim/vim/tree/master/src/xxd
    """

    def __init__(self):
        self.version = '0.1.0'

    def get_parser(self):
        parser = super().get_parser(description='darkbox xxd')
        parser.add_argument('file', nargs='?')
        parser.add_argument('-r', '--reverse', action='store_true')
        parser.add_argument('-u', '--uppercase', action='store_true')
        parser.add_argument('-p', '--plain', action='store_true')
        parser.add_argument('-c', '--cols', type=int, default=16)
        return parser

    @staticmethod
    def sidebar_str(s):
        return ''.join(chr(i) if 0x19 < i < 0x7f else '.' for i in s)

    def run(self, args=None):
        args = self.get_args(args)

        file_path = args['file']
        if not file_path:
            self.get_parser().print_help()
            return
        if os.path.isdir(file_path):
            self.directory_error(file_path)
            return
        if not os.path.isfile(file_path):
            self.file_not_found_error(file_path)
            return

        with open(file_path, 'rb') as f:
            line_counter = 0
            while True:
                raw_line = f.read(args['cols'])
                if not raw_line:
                    break # line is empty; EOF
                hex_line = binascii.hexlify(raw_line).decode('utf-8')

                if args['uppercase']:
                    hex_line = hex_line.upper()
                if args['plain']:
                    print(hex_line, end='')
                else:
                    hex_line = ' '.join(hex_line[i:i+4] for i in range(0, len(hex_line), 4))
                    hex_counter = hex(line_counter * args['cols'])[2:].zfill(8)
                    print(f'{hex_counter}: {hex_line}  {self.sidebar_str(raw_line)}')

                line_counter += 1

        print()
