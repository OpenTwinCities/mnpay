"""convert_utf16_to_utf8.py

Usage:
    convert_utf16_to_utf8.py <input_file> <output_file>
"""
from docopt import docopt
import csv


def main(input_file, output_file):
    with open(input_file, 'rb') as source_file:
        with open(output_file, 'w+b') as dest_file:
            contents = source_file.read()
            dest_file.write(contents.decode('utf-16').encode('utf-8'))


if __name__ == "__main__":
    arguments = docopt(__doc__)
    main(arguments["<input_file>"], arguments["<output_file>"])
