#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import urllib

from BeautifulSoup import BeautifulSoup


resp = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php')
soup = BeautifulSoup(resp.read())

prefix = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
r = re.compile(r'[^\d](\d+)[^\d]?')
r2 = re.compile(r'Divide')
start = soup.find(name='a').get(key='href')
now = r.search(start).group(1)

for i in range(400):
    url = '%s?nothing=%s' % (prefix, now)
    resp = urllib.urlopen(url).read()
    print 'request: %s' % url
    print 'response: %s' % (resp)
    if r2.search(resp):
        print 'divided'
        now = int(now) / 2
        continue
    n = r.findall(resp)[-1]
    if not n:
        break
    now = n
