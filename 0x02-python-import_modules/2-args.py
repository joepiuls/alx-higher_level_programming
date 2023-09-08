#!/usr/bin/python3
from sys import argv
argc = len(argv) - 1
if argc < 2:
    print("{} arguments.".format(argc))
else:
    if argc == 2:
        print("{} arguments:".fromat(argc))
    else:
        print("{} arguments:".format(argc))
    for i in range(1, argc+1):
        print("{}: {}".format(i, argv[i]))
