# -*- coding: utf-8 -*-
import sys

PY2 = sys.version_info[0] == 2

if PY2:
    # noinspection PyCompatibility
    iteritems = lambda d: d.iteritems()
else:
    iteritems = lambda d: iter(d.items())
