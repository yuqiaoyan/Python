#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      boyu
#
# Created:     15/11/2011
# Copyright:   (c) boyu 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import twitter
from twitter.oauth_dance import oauth_dance
import json

def makeTwitterRequest(t, twitterFunction, max_errors=3, *args, **kwArgs):
    wait_period = 2
    error_count = 0
    while True:
        try:
            return twitterFunction(*args, **kwArgs)
        except twitter.api.TwitterHTTPError, e:
            error_count = 0
            wait_period = handleTwitterHTTPError(e, t, wait_period)
            if wait_period is None:
                return
        except URLError, e:
            error_count += 1
            print >> sys.stderr, "URLError encountered. Continuing."
            if error_count > max_errors:
                print >> sys.stderr, "Too many consecutive errors...bailing out."
                raise

def getUserInfo(t,screen_names):
    info=[]
    response=makeTwitterRequest(t,t.users.lookup,screen_name=','.join(screen_names))

    for user_info in response:
        return user_info

def main():
    consumer_key="ePqZbaPwLRl0niYtMkJnTA"
    consumer_secret = "e6CiesDpGiEmkiZ2IGIZP7YGZa0BSLcNvrTWN6ySGU"
    oauth_token ="248987806-ezE8mY1ltnwNQVoL2ynv3lN1KOonbMKbfvYLXa7o"
    oauth_token_secret="aPBJozHLfF5gqMWRmTdRxDomtD417rDC95Bw1w1lY"
    #(oauth_token, oauth_token_secret) = oauth_dance('508 project',consumer_key,consumer_secret)
    #twit_api=twitter.Twitter(domain='api.twitter.com',api_version='1',auth=twitter.oauth.OAuth(oauth_token,oauth_token_secret,consumer_key,consumer_secret))
    twit_api=twitter.Api(consumer_key='consumer_key',
                  consumer_secret='consumer_secret',
                  access_token_key='oath_token',
                  access_token_secret='oath_token_secret')

    #a=getUserInfo(twit_api,"yuqiaoyan")
    #print a['friends_count']
    #print a['followers_count']
    #print a
    test=twit_api.GetHomeTimeline()


if __name__ == '__main__':
    main()
