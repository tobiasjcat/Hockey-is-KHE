#!/usr/bin/env python3

#Paul Croft
#September 10, 2020

import string
import sys

def main():
    basestring = None
    with open("base.svg") as infile:
        basestring = infile.readlines()


    string.ascii_letters
    splitone = 'glyph unicode="'
    # print(basestring[:10])

    doublelower = string.ascii_lowercase * 2
    doubleupper = string.ascii_uppercase * 2

    for i in range(26):
        with open("svgs/rot{}.svg".format(i),'w') as outfile:
            for bl in basestring:
                if splitone not in bl:
                    outfile.write(bl)
                else:
                    test_chr = bl[16]
                    test_val = ord(test_chr)
                    # print("HERE", test_chr)
                    if test_chr in string.ascii_letters:
                        if test_chr in string.ascii_lowercase:
                            new_char = doublelower[(test_val - 96) + i]
                        else:
                            new_char = doubleupper[(test_val - 64) + i]
                        # print("{} -> {}".format(test_chr, new_char))
                        outfile.write(bl[:16])
                        outfile.write(new_char)
                        outfile.write(bl[17:])
                    else:
                        outfile.write(bl)
    return 0

if __name__ == '__main__':
    exit(main())
