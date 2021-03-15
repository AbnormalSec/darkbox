#!/usr/bin/env python

"""darkbox"""

import sys
import importlib

__version__ = '0.1.0'

if sys.version < '3':
    print('Error: darkbox is only compatible with Python 3.')
    sys.exit(1)

import darkbox.commands as commands


def print_usage():
    print('Usage: darkbox <tool> [OPTIONS]')
    tools = [t for t in dir(commands) if not t.startswith('__')]
    tools.remove('template')
    print(f'Tools: {", ".join(tools)}')


def main():
    if len(sys.argv) == 1:
        print_usage()
        return

    cmd_name = sys.argv[1].strip().lower()
    if cmd_name in ['-v', '--version', 'version']:
        print(f'darkbox v{__version__}')
        return
    if cmd_name in ['-h', '--help', 'help']:
        print_usage()
        return

    try:
        cmd_module = importlib.import_module(f'darkbox.commands.{cmd_name}')
    except ModuleNotFoundError:
        print('Error: Tool not found!')
        return

    cmd = getattr(cmd_module, cmd_name)
    sys.argv = sys.argv[1:]
    c = cmd()
    c.run()


if __name__ == '__main__':
    main()
