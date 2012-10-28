#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      boyu
#
# Created:     05/02/2012
# Copyright:   (c) boyu 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import logging
import string
import re
import os
import timeit
import shutil

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
            ebayFilePath="/storage/eadar/projects/tsunami/ebay/completed"
            for filename in os.listdir(ebayFilePath):
                subDir=ebayFilePath+"/"+filename
                #read in the initial.html and save it to a string
                initialDataF = open(subDir+"/initial", 'r')
                text=initialDataF.read()
                #print len(text)
                if(string.find(text,"potassium")>=0):
                    shutil.copytree(subDir,"potassium2/"+filename)
        except Exception, err:
            print type(err)
            print (err.args)
            raise
            logging.debug(type(err))
        print "%.2f usec/pass" % (1000000 * t.timeit(number=100000)/1000000)

if __name__ == '__main__':
    main()
