#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import wave

m = "bbb8b499a0eef99b52c7f13f4e78c24b"
def decode():
    data = ''.join(open('bin.txt', 'r').readlines())
    return base64.b64decode(data)

d = decode()
open('india.wav', 'wb').write(d)

# didn't work
#def sorry():
#    c = httplib2.Http()
#    header, resp = c.request('http://www.pythonchallenge.com/pc/stuff/violin.php', headers={'cookie': 'info=%s' % 'sorry'})
#    print header, resp
#
#sorry()

w = wave.open('india.wav', 'r')
w2 = wave.open('india2.wav', 'w')
w2.setnchannels(w.getnchannels())
w2.setsampwidth(w.getsampwidth())
w2.setframerate(w.getframerate())
w2.writeframes(w.readframes(w.getnframes())[0::2])
