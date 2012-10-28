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
import os
import time

def main():
        try:
            os.system("python F:\\activepython26\\Lib\\site-packages\\pdfminer-20110515\\tools\\pdf2txt.py -o output.txt F:\Dropbox\Michigan\SI650InfoRetrieval\project\FriendsandNeighborsontheWeb.pdf")
            time.sleep(100)
            os.system("cd")
            time.sleep(100)
        except Exception as err:
            print type(err)
            print err.args

if __name__ == '__main__':
    main()
