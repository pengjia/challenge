#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle


p = pickle.Unpickler(open('peak.txt', 'r'))
o = p.load()

print '\n'.join([''.join([c * co for c, co in l]) for l in o])

