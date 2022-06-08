#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for ki, value in list(a_dictionary.items()):
        if ki == key:
            del a_dictionary[key]
    return a_dictionary
