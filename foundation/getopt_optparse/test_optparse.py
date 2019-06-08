import sys
from optparse import OptionParser

parser = OptionParser("install.py [--ip x.x.x.x] [--silent] [--help]")
parser.add_option("-s", "--ip",
                  action="store",
                  type="string",
                  dest="ip",
                  help="server ip"
                  )
parser.add_option("-t", "--silent",
                  action="store_true",
                  dest="silent",
                  help="silent"
                  )

# (option, args) = parser.parse_args(sys.argv)
argv = ["-s", "1.2.3.4", "-t", "extra"]
(option, args) = parser.parse_args(argv)

print(option.ip)
print(option.silent)
print(args)
