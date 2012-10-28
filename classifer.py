import math
import re
wordPattern=re.compile(r"([\w]+|[^\w\s]+)")
stopWordsList=[word.strip() for word in open("stoplist.txt","r")]

def tokenizeWord(text):
#function to tokenize the words
	wordList = wordPattern.findall(text)
	wordList = [word for word in wordList \
					if word not in stopWordsList]
	return(wordList)

class classifier:
	def __init__(self,filename = None):
	#Counts of words in each category
	#sample: wordClass["joy"]{"positive": 10, "negative": 1}
		self.wordClass  = {}
		self.defaultLaplace = 0.001
		self.defaultWeight = 0.1
		self.results = ""
		self.catCount = {}
		self.wordCount = 0	#keeps track of total words in collection
		#self.categoryCount = {}
	
	def incWC(self, category, word):
	#update our wordClass dictionary for each word increment its category count
		# if the word is not in the dictionary yet, then set it equal to an empty dic
		self.wordClass.setdefault(word, {})
		
		#set the default to .001 to eliminate the possibility of zeroes
		#this is similar to Laplace smoothing where we start off every1 at one
		self.wordClass[word].setdefault("positive",self.defaultLaplace)
		self.wordClass[word].setdefault("negative",self.defaultLaplace)
		
		#now we have a dict for each word, add one to the category
		self.wordClass[word][category] += 1
	
	def processDocument(self,document):
	#given a document, first char is category, after tab is text
	#1\t    Coming soon to a neighborhood near you...    MoveOn.org Bake Sales!
		category, text = document.split('\t')
		wordList = tokenizeWord(text)
		for word in wordList:
			self.wordCount += 1	#for every word in the document increment 1
			if( int(category) == 1 ):
				self.incWC("positive", word)
				self.catCount["positive"] = self.catCount.setdefault("positive",0)+1
			else:
				self.incWC("negative", word)
				self.catCount["negative"] = self.catCount.setdefault("negative",0)+1

	def loadTraining(self,filepath):
	#load some test data based on filename
		fileHandler = open(filepath, "r")
		for line in fileHandler:
			self.processDocument(line.strip())
		#for i in range(0,100):
		#	self.processDocument(fileHandler.readline().strip())
		fileHandler.close()
		
	def condProb(self,word, category):
	#returns p(w = word | c = category)
		totalWords = 0.0
		try:
			#get the counts for every category for the word
			categoryCounts = self.wordClass[word]
			
			#sum up the total words for given word to calculate probability
			for cat,count in categoryCounts.items():
				totalWords += count

			probability = 0
			try:
				#use Laplace smoothing + words seen for category / total words in corpus
				probability = (self.wordClass[word][category]) / (totalWords)
				print "the probability of '" + category + "' given " + word + " is :"
				print "p(" + category + "|" + word + ") = " + str(probability)
				return ( probability )
			except:
				#print "the '" + category + "' category does not exist for this word"
				#probability = 1 / (totalWords + 1.0)
				print "p(" + category + "|" + word  + ") = " + str(probability)
				return (probability)
		except:
			print "Word does not exist in our index"
			#probability = 1 / (totalWords + 1.0)
			probability = .5
			print "p(" + category + "|" + word + ") = " + str(probability)
			return ( probability )
	
	def getPCat(self,category):
	#P( category ) = total words in category / total words in document
		return(self.catCount[category]*1.0 / self.wordCount*1.0 )
	
	def bayesProb(self,word,category):
	#P(cat | doc ) = P( doc | cat ) * P( cat )
	#P(doc | cat ) = total counts of word in given category / total words in cat
		try:
			#print "word is " + word + " for " + category
			#print self.wordClass[word][category]
			probCatGivenTerm = (1.0*self.wordClass[word][category]+1.0) / (self.catCount[category]*1.0+len(self.wordClass))
			probability = probCatGivenTerm
			#print "the probability of '" + category + "' given " + word + " is :"
			#print "p(" + category + "|" + word + ") = " + str(probability)
			#print word + ": " + str(math.log(probability))
			return( math.log(probability) ) 
		except:
			#raise
			#word does not exist in the index so give it a +1 count
			probability = (1 / (1.0*len(self.wordClass)+self.wordCount))
			#print word + " does not exist: " + str(math.log(probability))
			return math.log(probability)
		
		
	def getWC(self):
		return(self.wordClass)
	
	def printWC(self):
	#print my wordClass for debug purposes
		print self.wordClass
	
	def printResults(self):
		print "Results is: "
		print self.results
		print "Category counts is: "
		print self.catCount
		resultFile = open("/Users/boyu/Dropbox/Michigan/SI650InfoRetrieval/hw3/resultNaive3.csv","w")
		resultFile.write(self.results)
		resultFile.close()
	
	def getClassification(self,document):
		tokenList = tokenizeWord(document)
		negProb = math.log(self.getPCat("negative"))
		#calculate probability for the sample being negative
		for word in tokenList:
			negProb += self.bayesProb(word,"negative")
	
		posProb = math.log(self.getPCat("positive"))
		#calculate probability for the sample being positive
		for word in tokenList:
			posProb += self.bayesProb(word,"positive")

		#print "Probability of '" + document + "' being positive is " + str(posProb)
		#print "Probability of '" + document + "' being negative is " + str(negProb)
		
		if( posProb > negProb):
			self.results += "1\n"
		else:
			self.results += "0\n"

#this classifier uses multinomial model
#p(mood = "positive | w = 'joy') = (total counts of positive)/ (total words in joy) 
test = classifier()
test.loadTraining("/Users/boyu/Dropbox/Michigan/SI650InfoRetrieval/hw3/training.txt")
#a = test.getWC()
filepath = "/Users/boyu/Dropbox/Michigan/SI650InfoRetrieval/hw3/testdata.txt"
#i = 0
for document in open(filepath,"r"):
	test.getClassification(document.strip())
	#if i > 1:
	#	break
	#i+=1
	
test.printResults()
#test.printWC()
