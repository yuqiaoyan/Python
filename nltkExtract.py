#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      boyu
#
# Created:     02/03/2012
# Copyright:   (c) boyu 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import logging
import string
import re
import pickle
import pprint
import nltk
import timeit

#Regular Expression Patterns
#abstractPattern     =   re.compile(r"abstract(.*?)^\n",(re.IGNORECASE | re.MULTILINE | re.DOTALL))
abstractPattern     =   re.compile(r"abstract(.*?)^\r\n",(re.IGNORECASE | re.MULTILINE | re.DOTALL))
keywordPattern		=	re.compile(r"(?:keywords?|index)(.*?)^\r\n",(re.IGNORECASE | re.MULTILINE | re.DOTALL))

def nameEntityExtract(document):
	sentences = nltk.sent_tokenize(document)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
	print sentences[0]
	print "the length of sentences is: " + str(len(sentences))
	sent = sentences[0]
	print nltk.ne_chunk(sent,binary=True)

def main():
	s = """\
            try:
                str._nonzero_
            except AttributeError:
                pass
            """
        t=timeit.Timer(stmt=s)

	try:
		fileData = open("output.txt").read()
		
		#print fileData
		abstractText    = abstractPattern.findall(fileData)[0]
		
		#keywordText is comma seperated text that includes the professors interests
		if(keywordPattern.findall(fileData) > 0):
			keywordText	= keywordPattern.findall(fileData)[0] 
		
		nameEntityExtract(fileData)
		
		
		
		#print abstractText, keywordText
	except Exception as err:
		print type(err)
		print err.args
		raise
        
	print "%.2f usec/pass" % (1000000 * t.timeit(number=100000)/1000000)
    
if __name__ == '__main__':
    main()
