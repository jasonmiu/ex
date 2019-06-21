#!/bin/env python3

sets = []

def powerset(s, cur_set, idx):



    if idx >= len(s):
        if len(cur_set) > 0:
            sets.append(cur_set)
        return


    c = cur_set.copy()

    # for each element, it can be added to current subset, or not
    powerset(s, c + list(s[idx]), idx + 1)
    powerset(s, c, idx+1)




if __name__ == "__main__":
    import sys

    powerset(list(sys.argv[1]), [], 0)

    print(sets)
