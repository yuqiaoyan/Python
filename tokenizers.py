import re

exception = "\xe2\x80\x99\x93"
wordPattern = re.compile(r"[a-zA-Z'-%s]+|[?!]"%exception)

def tokenize_sentence(text):
#function to tokenize the words
	wordList = wordPattern.findall(text)
	tokenized_word_list = []
	for word in wordList:
		word = word.lower()
		if word not in stopWordsList:
			tokenized_word_list.append(word)
	#wordList = [word.lower() for word in wordList \
	#				if word not in stopWordsList]
	return(tokenized_word_list)