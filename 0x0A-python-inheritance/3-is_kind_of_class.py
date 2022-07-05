#!/usr/bin/python3

"""
Function that checks if object is an instance of a specified class
Or a class that inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns:
        True if the obj is an instance of a_class
        False if otherwise.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
