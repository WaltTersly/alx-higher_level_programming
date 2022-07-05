#!/usr/bin/python3

""" Function that checks if object is an instance of a class """


def is_same_class(obj, a_class):
    """
    Returns:
        True if the obj is an instance of a_class
        False if otherwise.
    """

    if type(obj) == a_class:
        return True
    else:
        return False
