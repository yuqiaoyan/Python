a = "the cat"
b = "ca"
c = "c"

max_sentence = len(a)

def bucketize(a_list,pos):
	#buckets = [ [] for i in range(max_sentence) ]
	buckets = {}

	for sentence in a_list:
		if(len(sentence)-1 < pos):
			if(buckets.get(0)):
				buckets[0].append(sentence)
			else:
				buckets[0]=[sentence]
		else:
			key = ord(sentence[pos])
			print "char for key ", sentence[pos]
			if(buckets.get(key)):
				buckets[key].append(sentence)
			else:
				buckets[key]=[sentence]
	
	return buckets

test = [a,b,c]

for char_pos in range(max_sentence,-1,-1):
	buckets = bucketize(test,char_pos)
	sorted_keys = buckets.keys()
	sorted_keys.sort(reverse = False)
	#merge buckets
	result = []
	for bucket in sorted_keys:
		print bucket
		result= result + buckets[bucket]
	test = result

print result
