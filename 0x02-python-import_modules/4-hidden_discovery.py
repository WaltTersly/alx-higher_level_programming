#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    arry = dir()
    for i in range(0, len(arry)):
        if arry[i][0:2] != "__":
            print("{}".format(arry[i]))
