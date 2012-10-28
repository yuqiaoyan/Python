#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      boyu
#
# Created:     18/10/2011
# Copyright:   (c) boyu 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import networkx
import re
import twitter
import json
import sys
import pydoc
import time
from time import gmtime, strftime

def tsearch(query):
##Accepts a search query from a user to twitter. I am using this to input a search query for a user
##Returns JSON data from twitter API for query
    twitter_search=twitter.Twitter(domain="search.twitter.com")
    search_results=[]
    for page in range(1,15):
    	search_results.append(twitter_search.search(q=query, rpp=100,page=page))

    return json.dumps(search_results, sort_keys=True, indent=1)

def main():
##    t= pydoc.help(twitter)
##    twitters = twitter.Twitter(auth=twitter.OAuth(token, token_key, con_secret, con_secret_key))
##    x = twitters.statuses.public_timeline()
##    print x
##    print twitter.statuses.friends_timeline(id="KeroneWalkerMD")

##    twitter_api=twitter.Twitter(domain="api.twitter.com",api_version='1')
##    t=twitter_api.GetLists()

##
    x = strftime("%m_%d_%H%M%S", gmtime())
    #x= str(time.clock())
    fname="F:/test/halloween_"+x+".txt"
    #fname_gadd="F:/test/GadDafi_"+x+".txt"
    #fname_qadh="F:/test/QadHafi_"+x+".txt"

    search_results=tsearch("halloween")
##
    f = open(fname, 'w')
    f.write(search_results)
    f.close()


##    print search_results
##    print 'test'

if __name__ == '__main__':
    main()