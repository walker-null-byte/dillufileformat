import sys
from misc.cli_options import get_some_help, help, version, export, extract, list, commands


def main():
    if len(sys.argv) < 2:
        get_some_help()

    elif len(sys.argv) == 2:
        if sys.argv[1] not in commands:
            get_some_help()
        elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
            help()
        elif sys.argv[1] == '--version' or sys.argv[1] == '-v':
            version()
    
    elif len(sys.argv) == 3:
        if sys.argv[1] == '--export' or sys.argv[1] == '-e':
            export(sys.argv[2], sys.argv[2] + ".dillu")
        elif sys.argv[1] == '--list' or sys.argv[1] == '-l':
            list(sys.argv[2])
        elif sys.argv[1] == '--extract' or sys.argv[1] == '-x':
            extract(sys.argv[2], sys.argv[2] + "_extracted")
    
    elif len(sys.argv) == 4:
        if sys.argv[1] not in commands:
            get_some_help()
        elif sys.argv[1] == '--export' or sys.argv[1] == '-e':
            export(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == '--list' or sys.argv[1] == '-l':
            for i in sys.argv[2:]:
                list(i)
        elif sys.argv[1] == '--extract' or sys.argv[1] == '-x':
            extract(sys.argv[2], sys.argv[3])
        

if __name__ == '__main__':
    main()
