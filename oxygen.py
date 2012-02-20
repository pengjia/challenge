#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image
import string
import re

def compress(l):
    res = [l[0]]
    last = l[0]

    for c in l:
        if c == last:
            continue
        last = c
        res.append(c)

    return res

im = Image.open('oxygen.png')
data = im.getdata()

res = []
line = 0
width, height = im.size
for h in range(0, height):
    r = []
    for w in range(width * h, width * (h + 1)):
        d = data[w]
        if d[0] == d[1] and d[0] == d[2]:
            r.append(d[0])

    if len(r) > len(res):
        res = r
        line = h

t = string.maketrans('', '')
res = ''.join([t[c] for c in res[0::7]])

res = eval(re.compile(r'\[(.+)\]').search(res).group(1))
print ''.join([t[c] for c in res])
