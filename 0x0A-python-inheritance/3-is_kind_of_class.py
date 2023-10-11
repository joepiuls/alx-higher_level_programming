#!/usr/bin/python3
"""Definition of a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): check object.
        a_class (type): The class that match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class returnTrue.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
