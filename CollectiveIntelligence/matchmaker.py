#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bonnie
#
# Created:     24/08/2011
# Copyright:   (c) Bonnie 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

class matchrow:
#puts all data into a list
    def __init__(self,row,allnum=False):
        if allnum:
            #float the values if all the values are numbers based on all num param
            self.data=[float(row[i]) for i in range(len(row)-1)]
        else:
            self.data=row[0:len(row)-1]
        #get the match info into the matchrow object
        self.match=int(row[len(row)-1])

def loadmatch(f,allnum=False):
#wrapper function that will feed the info to the matchrow class
    rows = []
    for line in file(f):
##        print line
        rows.append(matchrow(line.split(','),allnum))
    return rows

def printSN(s,num):
    print(s+str(num))

def lineartrain(rows):
    averages = {}
    counts = {}

    for row in rows:
        #Get the class of this point
        cl = row.match

        averages.setdefault(cl,[0.0]*(len(row.data)))
        counts.setdefault(cl,0)

        #Add this point to the averages
        for i in range(len(row.data)):
            averages[cl][i]+=float(row.data[i])

        #Keep track of how many points in each class
        counts[cl]+=1

    for cl,avg in averages.items():
        for i in range(len(avg)):
            avg[i]/=counts[cl]

    return averages

    printSN("averages is",averages)
    printSN("counts is",counts)

#get objects of matchrows
agesonly=loadmatch('agesonly.csv',allnum=True)
ages=lineartrain(agesonly)
##matchmaker=loadmatch("matchmaker.csv")
print ages

