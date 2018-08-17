import sys
import tweepy

# Pegando a consulta por parâmetro
consulta = sys.argv[1:]

#Autenticações
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

#Login na API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Coletando tweets
def coletor(user):

    stuff = api.user_timeline(screen_name = user, count = 100, include_rts = True)

    for status in stuff:
        print status.author, status.user
