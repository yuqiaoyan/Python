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

#Regular Expression Patterns
abstractPattern     =   re.compile(r"abstract(.*?)^\n",(re.IGNORECASE | re.MULTILINE | re.DOTALL))

def main():
        try:
            fileData = open("F:\\Dropbox\\Michigan\\SI650InfoRetrieval\\project\\output.txt").read()
            #print fileData
            abstractText    = abstractPattern.findall(fileData)[0]
        except Exception as err:
            print type(err)
            print err.args
            raise

if __name__ == '__main__':
    main()
