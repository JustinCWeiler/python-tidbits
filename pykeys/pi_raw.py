#!/usr/bin/python

nargs = 6
def generator(args):
    q, r, t, k, n, l = args[0], args[1], args[2], args[3], args[4], args[5]
    t = 1 if t == 0 else t
    l = 1 if l == 0 else t
    while True:
        if 4*q + r - t < n*t:
            yield n
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
