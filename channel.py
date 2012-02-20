#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import zipfile

z = zipfile.ZipFile('channel.zip')
r = re.compile(r'[^\d](\d+)')
print z.read('readme.txt')
now = re.compile(r'[^\d](\d{5})').findall(z.read('readme.txt'))[-1]

cs = []
while True:
    fn = '%s.txt' % now
    cs.append(z.getinfo(fn).comment)
    now = r.findall(z.read(fn))
    if not now:
        break
    now = now[-1]

print ''.join(cs)
