#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib2
import re
import bz2
import urllib
import xmlrpclib

def eat():
    c = httplib2.Http()
    nothing = 12345
    infos = []
    while True:
        header, resp = c.request('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s' % nothing)
        infos.append(re.compile(r'info=([^;]+);').search(header['set-cookie']).group(1))
        r = re.compile(r'next busynothing is (\d+)').search(resp)
        if r:
            nothing = r.group(1)
        else:
            print resp
            break

    print bz2.decompress(urllib.unquote_plus(''.join(infos)))

def call():
    c = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
    print c.phone('Leopold')

def info():
    c = httplib2.Http()
    header, resp = c.request('http://www.pythonchallenge.com/pc/stuff/violin.php', headers={'cookie': 'info=%s' % 'the flowers are on their way'})
    print header, resp

info()
