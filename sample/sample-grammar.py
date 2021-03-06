#!/usr/bin/python2

import os
import sys
import io
import pyauparser


def main():
    # load a grammar file and dump contents to stdout

    g = pyauparser.Grammar.load_file("data/operator.egt")
    s = io.StringIO()
    g.export_to_txt(s)
    print(s.getvalue().encode("ascii", errors="replace"))


if __name__ == "__main__":
    main()
