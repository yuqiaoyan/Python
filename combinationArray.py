#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      boyu
#
# Created:     11/01/2012
# Copyright:   (c) boyu 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def permute(s):
    all =[]
    #for case 2 swap the characters
    permutation = []
    if(len(s) == 2):
        permutation=[s[0]+s[1],s[1]+s[0]]
        return permutation
    for i in range(0,len(s)):
        permutation=permute(s.translate(None,s[i]))
        for word in permutation:
            all.append(s[i] + word)
    return all

def permuteB(s):
    permutation=[]
    for c in s:
        words=permuteB(s.translate(None,c))
        if(len(words) ==0):
            return c
        for word in words:
            permutation.append(c + word)
    return permutation

def permuteCHelper(s,permutations):
    for c in s:
        words=permuteCHelper(s.translate(None,c),permutations)
        if(len(s) ==0):
            permutations.append()
            return ""
        for word in words:
            permutations.append(c + word)
            print c+word
    return permutations

def permuteC(s):
    permutations = []
    return permuteCHelper(s,permutations)

def main():
    word="ABCD"
    permutations = permuteC(word)
    print permutations
    print len(permutations)

    permutations = permute(word)
    print permutations

##    words = ""
##    for word in words:
##        print "b"

if __name__ == '__main__':
    main()
