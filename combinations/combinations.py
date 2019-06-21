#!/bin/env python3

def combin_iter(elements, r):

    combins = []
    n = len(elements)


    for i in range(0, n):

        if r == 1:
            combins.append(list(elements[i]))
        else:
            for next in combin_iter(elements[i+1:n], r-1):
                combins.append(list(elements[i]) + next)


    return combins

def combin(elements, r):
    print(combin_iter(elements, r))

if __name__ == "__main__":
    import sys

    combin(list(sys.argv[1]), int(sys.argv[2]))
