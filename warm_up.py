#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

WARM_UP = 'http://www.pythonchallenge.com/pc/def/0.html'

def getNextUrl(url):
    n = pow(2, 38)

    return re.compile('0').sub('%s' % n, url)


if __name__ == '__main__':
    print getNextUrl(WARM_UP)
