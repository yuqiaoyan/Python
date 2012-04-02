def sampletrain(cl):
	cl.train('Nobody owns the water.','good')
	cl.train('the quick rabbit jumps fences','good')
	cl.train('buy pharmaceuticals now','bad')
	cl.train('make quick money at the online casino','bad')
	cl.train('the quick brown fox jumps','good')

def getwords(doc):
	#split the string into a list of words by spaces
	words=[s.lower() for s in doc.split(' ')
	if len(s)>2 and len(s) <20]

	#return the unique set of words only
	return dict([(w,1) for w in words])

class classifier:
	def __init__(self,getfeatures,filename=None):
		#Counts of feature/category combinations
		self.fc={}
		#Counts of documents in each category
		self.cc={}
		self.getfeatures=getfeatures
			
	def incf(self,f,cat):
		self.fc.setdefault(f,{})
		self.fc[f].setdefault(cat,0)
		self.fc[f][cat]+=1
	
	def incc(self,cat):
		self.cc.setdefault(cat,0)
		self.cc[cat]+=1
	
	def train(self,item,cat):
		features=self.getfeatures(item)
		#increment the count for every feature with this category
		for f in features:
			self.incf(f,cat)
		
		#increment the count for this category
		self.incc(cat)
			
	def fcount(self,f,cat):
		if f in self.fc and cat in self.fc[f]:
			return float(self.fc[f][cat])
		return 0.0

def sim_pearson(prefs,p1,p2):
	si={}
	for item in 