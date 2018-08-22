""" darkbox xxd command """

from darkbox.commands.template import Command

import os
import binascii


class xxd(Command):
    def __init__(self):
        self.version = '0.0.1'

    def get_parser(self):
        parser = super().get_parser(description="produce or reverse hexdumps")
        parser.add_argument("-r", "--reverse", action="store_true")
        parser.add_argument("-u", "--uppercase", action="store_true")
        parser.add_argument("-p", "--plain", action="store_true")
        parser.add_argument("-c", "--cols", type=int, default=16)
        parser.add_argument("file", nargs='?')
        return parser
    
    @staticmethod
    def sidebar_str(s):
        return ''.join(chr(i) if 0x19<i<0x7f else '.' for i in s)

    def run(self):
        args = self.get_args()

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
                if not raw_line: break # line is empty; EOF
                hex_line = binascii.hexlify(raw_line).decode("utf-8")

                if args['uppercase']:
                    hex_line = hex_line.upper()

                if args['plain']:
                    print(hex_line, end='')

                else:
                    hex_line = ' '.join(hex_line[i:i+4] for i in range(0, len(hex_line), 4))
                    hex_counter = hex(line_counter * args['cols'])[2:].zfill(8)
                    print("{}: {}  {}".format(hex_counter, hex_line, self.sidebar_str(raw_line)))

                line_counter += 1

        print('')
