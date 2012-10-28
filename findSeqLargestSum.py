def findSeqLargestSum(a):
#given an array of integers (both positive and negative)
#Find the continuous sequence w/ the largest sum
#input: (2,-8,3,-2,4,-10)
#output: 5 - (3,-2,4)
	temp = 0
	max = 0
	start = []
	end = []
	seqIndex = 0
	
	for i in range(0,len(a)):
		temp += a[i]
		for j in range(i+1, len(a)):
			temp += a[j]
			print temp
			if( temp > max):
				start = []
				end = []
				max = temp
				start.append(i)
				end.append(j)
			elif(temp == max):
				seqIndex += 1
				start.append(i)
				end.append(j)
		print "Max is: " + str(max)
		print "i is: " + str(i)
		temp = 0
	
	print max
	print start
	print end
	
b = [2,-8,3,-2,4,-10,1,2,2]

findSeqLargestSum(b)
