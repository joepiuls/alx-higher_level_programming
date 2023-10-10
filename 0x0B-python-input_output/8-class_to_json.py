#!/usr/bin/python3
"""Definition a Python class-to-JSON func."""


def class_to_json(obj):
    """Return the dictionary in a simple data structure."""
    return obj.__dict__
