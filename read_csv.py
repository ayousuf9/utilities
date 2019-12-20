#!/usr/bin/env python

import csv
from argparse import ArgumentParser

p = ArgumentParser(description='Read csv file')
p.add_argument('-f', '--file_name', required=True,
help='Provide csv file name')
args = p.parse_args()

print('Here is the file name: {}'.format(args.file_name))
