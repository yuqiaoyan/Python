#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bonnie
#
# Created:     14/08/2011
# Copyright:   (c) Bonnie 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def ispalindrome(num):
    y=str(num)
    numlen=len(y)

    if(y[0]!=y[-1]):
        return 0

    if numlen%2 ==0:
        loop = numlen/2
    else:
        loop=(numlen-1)/2

    for i in range(1,loop):
        if(y[i] != y[(i+1)*(-1)]):
            return(0)

    return(1)

def largestpalindrome(a,b):

    pal=0

    c=b
    while(a):
        while(b):
            if(ispalindrome(a*b) and (a*b)>pal):
                pal=a*b
            b-=1
        c-=1
        b=c
        a-=1

    return(pal)

def E5():
    a=22

#if it is divisible by 2 and it is divisible by 3 stop
    while((a%2)!=0 or (a%3)!=0 or (a%5)!=0 or (a%7)!=0 or (a%11)!=0 or (a%13)!=0 or (a%17)!=0 or (a%19)!=0 or(a%20)!=0 or(a%18)!=0 or (a%16)!=0 or (a%15)!=0 or (a%14)!=0 or (a%12)!=0 or (a%9)!=0 or (a%8)!=0 or (a%4)!=0):
        a+=22
    print a
    return(a)

E5()
##3120213 -> 7, 7/2 is odd, loop (7-1)/2 times
##4004 -> 4 4/2 4=4, 0=0 is palindrome
##    return(numlen)