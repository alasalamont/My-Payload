#!/usr/bin/env python3

import argparse
import os
from git_index_parser import GitIndexParser

# Set up the argument parser
parser = argparse.ArgumentParser(description='Dump ./git/index file into cleartext, readable')
parser.add_argument('index', nargs='?', default='./.git/index', help='Specify the path of .git/index file')
args = parser.parse_args()

# Check if the index file exists
if not os.path.isfile(args.index):
    print("[x] Missing file `index` at `.git/ directory`")
    exit(1)

# Parse the index file
try:
    index_file = GitIndexParser.parse_file(path_to_file=args.index)

    # Process each entry in the index file
    for entry in index_file.get_entries():
        split_names = entry.name.split(' ')
        print(' '.join(split_names))  # Joining the list into a string

except FileNotFoundError:
    print(f"Error: File {args.index} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
