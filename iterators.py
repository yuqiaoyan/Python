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

#an object is called an iterable object if you can get an iterator object from it
#use iter() function to take an arbitrary object and return an iterator

def main():
        logging.basicConfig(level=logging.DEBUG, filename='debug.log',
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
        try:
            L=[1,2,3]
            it=iter(L)  #it is an iterator object
            print it
            print type(L)
            M=[2,3,4]
            incrementList = [[i,j] for i in L for j in M]
            print incrementList
            newList=[]

            b="kitte"
            a="sitting"
            newList=[]
            for i in range(len(b)+1):
                test=[]
                for j in range(len(a)+1):
                    test.append(0)
                newList.append(test)
            print newList
        except Exception as err:
            print type(err)
            logging.debug(type(err))
            logging.debug(err.args)     #tells me the type of exception,arguments bound to the exception, the type of argument depends on the exception - you need to read Exception list to get the details


if __name__ == '__main__':
    main()
