#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import maketrans, ascii_lowercase

t = maketrans(ascii_lowercase, ascii_lowercase[2:] + ascii_lowercase[:2])

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. " \
        "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm " \
        "jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print s.translate(t)
print 'map'.translate(t)
