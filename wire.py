#!/usr/bin/env python
# -*- coding:utf8 -*-
# Last modified:

""" docstring
"""

import Image

__revision__ = '0.1'


vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]

im = Image.open('wire.png')
new = Image.new('RGB', (100, 100))
x, y = 0, 0
d = 0
last_step = 100
step = 100
t = 1
for data in im.getdata():
    step -= 1
    print x, y
    new.putpixel((x, y), data)
    if step == 0:
        d = (d + 1) % 4
        t -= 1
        if t == 0:
            last_step -= 1
            t = 2
        step = last_step

    x, y = (x + vector[d][0], y + vector[d][1])

new.save('wired.png')
