#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

data = ''.join(open('equality.txt', 'r').readlines())

print  ''.join(re.compile(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]').findall(data))
