import random
import sys
from numpy import*
from math import*
import matplotlib.pyplot as plt

#Each time you collect a coupon, you are equally likely to get type N coupon
#What is the expected # of coupons you have to collect, so you can
#complete a set of coupons?

def getNumCoupons(numType):
#give numType coupons, this function will return the number of
#coupons you have to collect
	numTypeList = [i for i in range(1,numType)]
	numObs = 0
	
	#once we remove all the items from the list we've completed the set
	while(numTypeList):
		obs = random.randint(1,numType)		
		numObs += 1
		if obs in numTypeList:
			try:
				numTypeList.remove(obs)
			except:
				print "Issue with random generator and numTypeList"

	return numObs

def simExperiments(num, numType):
#simulate num Experiments and save the collection of results in a list
#return the list of results
	result = []	
	
	#run the experiment num times
	for i in range(0,num):
		numCoupons = getNumCoupons(numType)	#define numType of coupons in cmd line
		result.append(numCoupons)
		print "Coupons is: " + str(numCoupons)
	return numCoupons

def drawHist(aHistogram):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.hist(aHistogram,normed=1,facecolor='green',alpha=0.75)
	plt.show()
	
if __name__ == '__main__':
#cmd line: 	"python probability.py numExperiments numCouponType"
#		#python probability.py 1000 7"
	types = int(sys.argv[2])
	resultList = simExperiments(int(sys.argv[1]),types)
	resultArray = array(resultList)
	print "The expected number of coupons for " + sys.argv[1] + " number of experiments is: "
	print str(mean(resultArray))
	print "The expected number based on GEOMETRIC DISTRIBUTION is: "
	print log(types)*types
	print "The expected number based on BINOMIAL DISTRIBUTION is: "
	print types*(1.0/types)*( pow((double(types - 1)/types),types-1))*types
	#drawHist(resultArray)
	drawHist(histogram(resultArray, bins = 10))
