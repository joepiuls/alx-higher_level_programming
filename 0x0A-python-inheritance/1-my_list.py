#!/usr/bin/python3
"""Definition an inherited list class MyList."""


class MyList(list):
    """Implement the sorting and printing."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
