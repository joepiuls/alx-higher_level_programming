#!/usr/bin/python3
"""Reads from standard input and computation of the metrics.

After every ten lines or the input of a keyboard interruption with (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int):  accumulated read file size.
        status_codes (dict):  accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

