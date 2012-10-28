#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bonnie
#
# Created:     28/01/2012
# Copyright:   (c) Bonnie 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def LeveDistance(a,b):
    #Levenshtein distance
    #calculate the edit distance between a and b
    #a is a string, b is a string
    editMatrix=[[0 for i in range(len(b)+1)] for j in range(len(a)+1)]

    #initialize the first values into the matrix
    for i in range(len(a)+1):
        editMatrix[i][0]=i

    for j in range(len(b)+1):
        editMatrix[0][j]=j


    for j in range(1,len(b)+1):
        for i in range(1,len(a)+1):
            if(a[i-1] == b[j-1]):
                editMatrix[i][j]=editMatrix[i-1][j-1]
            else:
                deletion=editMatrix[i-1][j]+1
                insertion = editMatrix[i][j-1]+1
                substitution=editMatrix[i-1][j-1]+1
                editMatrix[i][j]=min(deletion,insertion,substitution)

    return editMatrix[len(a)][len(b)]

print LeveDistance("hil","hi")
