#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image

im = Image.open('mozart.gif')
w, h = im.size

ds = im.getdata()
new = Image.new('RGB', im.size)
ds = [[ds[x + y * h] for x in range(w)] for y in range(h)]
for y, l in enumerate(ds):
    for i, d in enumerate(l):
        if d == 195:
            break
    for x, d in enumerate(l[i:] + l[:i]):
        new.putpixel((x, y), d)

new.save('mozart2.gif')
