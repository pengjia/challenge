#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import urllib

#from BeautifulSoup import BeautifulSoup

#f = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
#cont = f.read()
#open('ocr.txt', 'w').write(f.read())
cont = open('ocr.txt', 'r').read()
#soup = BeautifulSoup(cont)
#comment = soup.find(text=re.compile('\^\^'))
comment = cont
wc = {}
chars = []

for c in comment:
    wc.setdefault(c, 0)
    wc[c] += 1
    if wc[c] == 1:
        chars.append(c)

results = ''.join([c for c in chars if wc[c] == 1])
print results
