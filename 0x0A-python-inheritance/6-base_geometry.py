#!/usr/bin/python3
"""Definition of a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """if not implemented."""
        raise Exception("area() is not implemented")
