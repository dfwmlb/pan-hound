#!/usr/bin/env python

import os
import fnmatch
import sys
import re
import argparse

def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """

    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )

def find(cfg):

    search_pattern = re.compile("[45]\d{15}")

    for path, dirs, files in os.walk(os.path.abspath(cfg.dir)):
        for filename in fnmatch.filter(files, cfg.glob):
            pardir = os.path.normpath(os.path.join(path, '..'))
            pardir = os.path.split(pardir)[-1]
            filepath = os.path.join(path, filename)

            with open(filepath) as f:
                data = f.read()

            all_matches = search_pattern.findall(data)

            pan = []
            for str in all_matches:
                if cardLuhnChecksumIsValid(str):
                    pan.append(str)

            if pan:
                print '{} matches in {}'.format(len(pan), filepath)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='''DESCRIPTION:
    Find PAN matches recursively in files from the given folder''',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='''USAGE:
    {0} -d [my_folder] -g [glob_pattern]'''.format(os.path.basename(sys.argv[0])))

    parser.add_argument('--dir', '-d',
                        help='folder to search in; by default current folder',
                        default='.')

    parser.add_argument('--glob', '-g',
                        help='glob pattern, i.e. *.html',
                        default="*.*")

    config = parser.parse_args(sys.argv[1:])

    find(config)