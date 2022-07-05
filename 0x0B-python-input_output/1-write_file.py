#!/usr/bin/python3

""" Open and write into a file """


def write_file(filename="", text=""):
    """
    Args:
        filename (file): The file to write into.
        text (text): The text to write.
    Returns:
        Numner of characters written.
    """
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
