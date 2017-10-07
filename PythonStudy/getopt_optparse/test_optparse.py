from optparse import OptionParser

parser = OptionParser(
    "install.py [--sip x.x.x.x] [--pip x.x.x.x] [--help]")
parser.add_option("-s", "--sip",
                  action="store",
                  type="string",
                  dest="sip",
                  help="server ip"
                  )
parser.add_option("-p", "--pip",
                  action="store",
                  type="string",
                  dest="pip",
                  help="peer ip"
                  )

argv = ["-s", "1.2.3.4", "-p", "4.3.2.1"]
(option, args) = parser.parse_args(argv)

print option.sip
print option.pip
print args
