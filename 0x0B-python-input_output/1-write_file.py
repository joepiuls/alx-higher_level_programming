#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a str to a UTF8 text file.

    Args:
        filename (str): The name of the file.
        text (str): The text to write in the file.
    Returns:
        The num of char written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
