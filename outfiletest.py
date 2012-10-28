#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      boyu
#
# Created:     18/10/2011
# Copyright:   (c) boyu 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys

def main():

    x="test"
    f = open('F:/test/foo4.txt', 'w')
    f.write(x)
    f.close()


if __name__ == '__main__':
    main()
