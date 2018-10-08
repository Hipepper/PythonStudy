# -*- coding: utf-8 -*-
import sys
from optparse import OptionParser


def process_command_line(argv):
    """
    Return a 2-tuple: (settings object, args list).
    `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.
    """
    parser = OptionParser(argv[0] + " --file")
    parser.add_option('-f', '--file',
                      action='store',
                      type='string',
                      dest='file',
                      help='sample for input file!')
    parser.add_option('-q', '--quiet',
                      action='store_true',
                      dest='quiet',
                      help='sample for quiet option!')
    settings, args = parser.parse_args(argv)

    return settings, args


def main(argv):
    settings, args = process_command_line(argv)
    print("settings: " + str(settings))
    print("args: " + str(args))
    # application code here, like:
    # run(settings, args)
    return 0  # success


if __name__ == '__main__':
    test_argv = ["./optparse_cmd.py", "-h"]
    test_argv = ["./optparse_cmd.py", "-f", "test.file"]
    test_argv = ["./optparse_cmd.py", "-q"]
    status = main(test_argv)
    sys.exit(status)
