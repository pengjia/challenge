#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import difflib

ls = gzip.GzipFile('deltas.gz', 'rb').read().splitlines()

left, right = [], []
png = [[], [], []]

for l in ls:
    left.append(l[:53])
    right.append(l[56:])

for d in difflib.ndiff(left, right):
    bs = [chr(int(b, 16)) for b in d[2:].split()]
    if d[0] == '-':
        png[1].append(''.join(bs))
    elif d[0] == '+':
        png[2].append(''.join(bs))
    else:
        png[0].append(''.join(bs))

for i, p in enumerate(png):
    open('ball%s.png' % i, 'wb').write(''.join(p))
