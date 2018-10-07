import sys
import getopt


def getopt_sample():
    cmdline_params = [["-c test"], ["-h"], ["--config=configtest"]]

    opts, args = getopt.getopt(cmdline_params, 'hc:', ['help', 'config='])
    print(opts)
    print(args)
    for option, parameter in opts:
        if option == '-h' or option == '--help':
            print("This program can be run with either -h or --help for this message,")
            print("or with -c or --config=<file> to specify a different configuration file")
        if option in ('-c', '--config'):  # this means the same as the above
            print("Using configuration file %s" % parameter)


if __name__ == "__main__":
    getopt_sample()
