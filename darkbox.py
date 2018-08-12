""" darkbox """

import sys
import commands
import importlib


def main():
    if len(sys.argv) == 1:
        print("Usage: darkbox <tool> [OPTIONS]")
        print("Tools: {}".format(
            ', '.join([t for t in dir(commands) if not t.startswith('__')])
        ))
        return

    cmd_name = sys.argv[1]
    cmd_module = importlib.import_module('commands.{}'.format(cmd_name))
    cmd = getattr(cmd_module, cmd_name)
    sys.argv = sys.argv[1:]
    c = cmd()
    c.run()


if __name__ == '__main__':
    main()