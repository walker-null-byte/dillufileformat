from sys import exit
from .export_file import export_file
from .list_files import list_files
from .extract_file import extract_file
commands = {'--help', '--version', '--export', '--extract', '--list', '-h', '-v', '-e', '-x', '-l'}
LATEST_VERSION = "1.0.0"

def get_some_help():
    print("Invalid Usage")
    print("Usage: python main.py <command> <input_file> <output_file> <version>(Default = 1.0.0)")
    print("use --help/-h for more info")
    exit(1)

def help():
    print("Dillu File Format")
    print("Usage: python main.py <command> <input_file> <output_file> <version>(Default = 1.0.0)")
    print("\nCommands:")
    print("--help/-h : Show this help message")
    print("--version/-v : Show version")
    print("--export/-e : Export file")
    print("--extract/-x : Extract file")
    print("--list/-l : List files in the archive")
    exit(0)

def version():
    print("Dillu File Format Version: " + LATEST_VERSION)
    exit(0)

def export(filename, output_filename):
    export_file(filename, output_filename)
    exit(0)

def list(filename):
    list_files(filename)

def extract(filename, folder):
    data = list_files(filename)
    extract_file(filename, folder, data)
    exit(0)