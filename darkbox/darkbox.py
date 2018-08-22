#!/usr/bin/env python

""" darkbox """

import sys
import importlib

__version__ = '0.0.2'

if sys.version < '3':
    print("Error: darkbox is only compatible with Python 3.")
    sys.exit(1)
else:
    import darkbox.commands as commands


def print_usage():
    print("Usage: darkbox <tool> [OPTIONS]")
    tools = [t for t in dir(commands) if not t.startswith('__')]
    tools.remove('template')
    print("Tools: {}".format(', '.join(tools)))


def main():
    if len(sys.argv) == 1:
        print_usage()
        return

    cmd_name = sys.argv[1]
    if cmd_name in ['-v', '--version', 'version']:
        print('darkbox v{version}'.format(
            version=__version__
        ))
        return
    if cmd_name in ['-h', '--help', 'help']:
        print_usage()
        return

    try:
        cmd_module = importlib.import_module('darkbox.commands.{}'.format(cmd_name))
    except ModuleNotFoundError:
        print("Error: Tool not found!")
        return
    cmd = getattr(cmd_module, cmd_name)
    sys.argv = sys.argv[1:]
    c = cmd()
    c.run()


if __name__ == '__main__':
    main()
