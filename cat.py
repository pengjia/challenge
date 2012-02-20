#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

def is_loop_year(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

for year in range(1006, 2006, 10):
    if is_loop_year(year) == True:
        t = datetime.datetime(year, 1, 26)
        if t.weekday() == 0:
            print t
