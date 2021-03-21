#!/usr/bin/python

nargs = 1
def generator(args):
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    i = 0
    while True:
        if 4*q + r - t < n*t:
            if i >= args[0]:
                yield n
            else:
                i += 1
            nr = 10*(r - n*t)
            nn = 10*(3*q + r) // t - 10 * n
            q *= 10
            r = nr
            n = nn
        else:
            n = (q*(7*k + 2) + r*l) // (t*l)
            r = (2*q + r)*l
            q *= k
            t *= l
            l += 2
            k += 1
