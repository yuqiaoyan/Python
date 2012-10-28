#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      boyu
#
# Created:     02/03/2012
# Copyright:   (c) boyu 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import logging
import string
import re

def main():
        s = """\
            try:
                str._nonzero_
            except AttributeError:
                pass
            """
        t=timeit.Timer(stmt=s)
        logging.basicConfig(level=logging.DEBUG, filename='debug.log',
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
        try:

        except Exception as err:
            print type(err)
            logging.debug(type(err))
logging.debug(err.args)     #tells me the type of exception,arguments bound to the exception, the type of argument depends on the exception - you need to read Exception list to get the details
        print "%.2f usec/pass" % (1000000 * t.timeit(number=100000)/1000000)

if __name__ == '__main__':
    main()
