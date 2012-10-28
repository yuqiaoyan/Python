#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      boyu
#
# Created:     04/02/2012
# Copyright:   (c) boyu 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import logging
import string
import re
import timeit

#timing function example
s = "string. With. Punctuation"
exclude = set(string.punctuation)
table = string.maketrans("","")
regex = re.compile('[%s]' % re.escape(string.punctuation))

def test_set(s):
    return ''.join(ch for ch in s if ch not in exclude)

print "sets      :",timeit.Timer('f(s)', 'from __main__ import s,test_set as f').timeit(1000000)


if __name__ == '__main__':
    main()
