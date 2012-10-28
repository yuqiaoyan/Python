#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bonnie
#
# Created:     10/02/2012
# Copyright:   (c) Bonnie 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def printBFS(result):
    if(len(result)==0):
        return

    result[0].printValue()
    node = result.pop(0)
    if(node.getRight()!=None):
        print node.name, 'has right'
        result.append(node.right)
    if(node.getLeft()!=None):
        print node.name, 'has left'
        result.append(node.left)

    printBFS(result)


class Node:
    def __init__(self,name="",left=None,right=None,sibling=None):
        self.name=name
        self.left= left
        self.right=right
        self.sibling=sibling
    def setRight(self,right):
        self.right=right
    def setLeft(self,left):
        self.left=left
    def printValue(self):
        print self.name
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left

def main():
    B =  Node("B")
    #B.printValue()
    C= Node("C")
    A=Node("A",B,C)
    #A.printValue()
    D=Node("D",None,A)

    result=[D] #initialize queue
    #result[0].printValue()
    printBFS(result)

if __name__ == '__main__':
    main()
