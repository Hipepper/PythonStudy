import argparse

parser = argparse.ArgumentParser(description='this is a description')

parser.add_argument('--version', '-v',
                    required=True,
                    type=int,
                    help='version')
parser.add_argument('--silent', '-s',
                    action='store_true',
                    help='silent')

parser.add_argument('file',
                    choices=['test1', 'test2'])

parser.add_argument('--format',
                    nargs='?',
                    default='simple',
                    help='the output format')
args = parser.parse_args()
if args.silent:
    print("Ture")
else:
    print("False")

print("version: " + str(args.version))
print("file: " + args.file)
print("format: " + args.format)
#python ./argparse_demo.py -v 2 -s  --format ttt test2