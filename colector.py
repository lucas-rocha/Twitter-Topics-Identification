import sys
import tweepy

# Pegando a consulta por parâmetro
user = sys.argv[1:]

#Autenticações
consumer_key = '9JFv1iPBVFCsln8xcGZzsZKjf'
consumer_secret = 'EhIem9oJS7k7i9eeuoyH44qAeDKdI9NGrjRH6kxcbO1qskB1fq'

access_token = '207565253-xI3kWTZr9KERbuOxYO0BEnsOROQm37IzKu7RY4bK'
access_token_secret = 'tn1fWYTaVaICVPWbyssBjWwltnDTO4B7YddxJX3U2AM1x'

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
