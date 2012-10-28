#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      boyu
#
# Created:     14/01/2012
# Copyright:   (c) boyu 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import string

def saveToTxt(*args):
#accepts any number of arguments to save to file
    out=""
    string.join(args,'\t')

    out += '\n'
    return(out)

def saveListToTxt(aList):
    out=""
    for col in aList:
        out = out+col+'\t'

    #add the carriage return
    out += '\n'

def main():
    a=['a','b','c']
    saveToTxt('a','b','c')

if __name__ == '__main__':
    main()
