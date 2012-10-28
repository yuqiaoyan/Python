#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bonnie
#
# Created:     27/01/2012
# Copyright:   (c) Bonnie 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    s=[1,5,3,2]
    for i in range(3):
        j=i
        while(s[j]>s[j+1] and j>=0):
        #all element from a(o,i) is sorted
            a=s[j]
            s[j]=s[j+1]
            s[j+1]=a
            j-=1
    print s

if __name__ == '__main__':
    main()
