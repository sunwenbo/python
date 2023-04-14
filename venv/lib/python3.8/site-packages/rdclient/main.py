#!/usr/bin/env python3
# coding=utf-8

"""just run rd binary

"""

import sys
import os.path
import os


def main():
    this_dir = os.path.dirname(__file__)
    fn = os.path.join(this_dir, "rd")
    os.execv(fn, sys.argv)


if __name__ == '__main__':
    main()
