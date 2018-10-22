import sys
import tweepy

# Pegando a consulta por parâmetro
user = sys.argv[1:]

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
def coletor(user, amount = 200):

    stuff = api.user_timeline(screen_name = user, count = amount, include_rts = False, tweet_mode = 'extended')

    for status in stuff:
        print (status.full_text)

coletor('Harvard')
