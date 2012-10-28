import re
from nltk.corpus import stopwords

exception = "\xe2\x80\x99\x93"
word_pattern = re.compile(r"[a-zA-Z'-%s]+|[?!]"%exception)

def tokenize_sentence(text):
#function to tokenize the words
	word_list = word_pattern.findall(text)
	tokenized_word_list = []
	
	for word in wordList:
		word = word.lower()
		if word not in stopWordsList:
			tokenized_word_list.append(word)
	#wordList = [word.lower() for word in wordList \
	#				if word not in stopWordsList]
	return(tokenized_word_list)

def tokenize_sentence(sentence,unique_stop_words=[]):
	'''REQUIRES: a sentence
	unique_stop_words is a list of additional stop words you define e.g. ['wall','street']
	RETURNS: a list of tokens split by spaces without stop words
	'''

	words = []

	for word in sentence.split(' '):
		stopwords = stopwords.words('english')
		stopwords = stopwords + unique_stop_words 
		if not word.lower() in stopwords and len(word) > 2:
			words.append(word.lower())

	return words

def tokenize_text_list(text_list,unique_stop_words=[]):
#REQUIRES: text_list is a list of sentences; unique_stop_words is a list of additional stopwords you can define
#RETURNS: a list of tokens without stop words
    words = []
    for text in text_list:
        text = text.strip()
        #words = [word.lower() for word in text.split(' ') if not word.lower() in nltk.corpus.stopwords.words('english')]
        for word in text.split(' '):
            stopwords = stopwords.words('english')
            stopwords = stopwords + unique_stop_words 
            if not word.lower() in stopwords:
                words.append(word.lower())
    return words