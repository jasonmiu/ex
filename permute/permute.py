#!/bin/env python
def permute(a, start_idx, end_idx):

#    print "start_idx: %d" % (start_idx)


    if start_idx == end_idx:
        print a

    else:
        for i in range(start_idx, end_idx+1):
#            print "  i:", i

            # swap a[i] , a[start_idx]
            temp = a[i]
            a[i] = a[start_idx]
            a[start_idx] = temp

            permute(a, start_idx + 1, end_idx)

            # swap back a[i] , a[start_idx] for backtrack
            temp = a[i]
            a[i] = a[start_idx]
            a[start_idx] = temp

if __name__ == "__main__":
    import sys

    permute(list(sys.argv[1]), 0, len(sys.argv[1])-1)
