#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bonnie
#
# Created:     16/08/2011
# Copyright:   (c) Bonnie 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import urllib
import BeautifulSoup
from BeautifulSoup import *
import re

def main():
    webobject=urllib.urlopen("http://www.dance25.com")
    html = webobject.read()
    htmlparse = BeautifulSoup(html)

    tags = htmlparse('a')
##    for tag in tags:
##        print tag.get('href', None)

    urls=[tag.get('href') for tag in tags]

    pattern=re.compile(".*neoease\.com")

    for item in urls:
        result=pattern.search(item)
        print result
        print item
        if(result!=None):
            foundhtml=item

if __name__ == '__main__':
    main()
