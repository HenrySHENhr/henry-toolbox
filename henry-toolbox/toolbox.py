import sys

from .loader import load_csv_file


def run_cli(arguments=None):
    if arguments is None:
        arguments = sys.argv[1:]
    print('main', arguments)
