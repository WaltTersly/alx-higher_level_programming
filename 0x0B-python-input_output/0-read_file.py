#!/usr/bin/python3

""" Read file and print contents to stdout """


def read_file(filename=""):
    """
    Args:
        filename (file): The file to be read.
    """
    with open(filename, encoding="UTF8") as fl:
        for line in fl:
            print(line, end='')
