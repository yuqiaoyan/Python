#-------------------------------------------------------------------------------
# Name:        soshProblem
# Purpose:
#
# Author:      Bonnie
#
# Created:     10/02/2012
#-------------------------------------------------------------------------------

import sys

def insertInSortedArray(line,pos,topN):
#given a value and the position in which it needs to be inserted
#return a new sorted array
    newLine=line
    temp = topN[pos]
    while(pos >=0):
        topN[pos]=newLine
        newLine=temp
        temp=topN[pos-1]
        pos-=1
    return topN

def findPlace(value,topN):
#we use a basic linear search to find the position of the element for an insertion-sort method
#as long as N is small then, this will be a good option
#if N is expected to be large, then a binary search may be better

    for i,line in enumerate(topN):
        lenElem = len(line)
        if(value < lenElem):
            return i-1

    #if we've reached the end of the loop, then the value should be in the last index of topN
    lastIndex=len(topN)-1
    return lastIndex

def main(filename,N):
    fileA=open(filename, "r")

    #initialize an empty list array to hold the N largest sentences
    #TopN is a sorted array from smallest to largest
    topN = ['']*N

    for line in fileA:
        value=len(line)
        smallestElem=len(topN[0])
        if(value>smallestElem):
            pos=findPlace(value,topN)
            topN=insertInSortedArray(line,pos,topN)

    #print out the top N lines frmo the file
    print topN

if __name__ == '__main__':
    main(sys.argv[1],int(sys.argv[2]))
