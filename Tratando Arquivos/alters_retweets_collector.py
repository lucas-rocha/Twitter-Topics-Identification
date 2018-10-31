# -*- coding: utf-8 -*-
# -> Escrito para python 2 <- #
import tweepy, datetime, sys, time, os, os.path, shutil, time, struct, random, json
reload(sys)
sys.setdefaultencoding('utf-8')

#-------------------------------------------------------------------------#

def read_ego_bin(file):
	with open(file, 'r') as f:
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		alters_list = []
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			retweet, user = timeline_struct.unpack(buffer)
			if not user in alters_list:
				alters_list.append(user)
	return alters_list

#-------------------------------------------------------------------------#

def read_alter_bin(file):
	global alters_list
	global json_alter

	with open(file, 'r') as f:
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		tweet_id_list = []
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			retweet, user = timeline_struct.unpack(buffer)

			if (user in alters_list) and (not user == json_alter):
				tweet_id_list.append(retweet)
	return tweet_id_list

#-------------------------------------------------------------------------#

def collect_and_save(tweet_id_list, ego):
	global json_alter

	file = output + ego + '.json'
	with open(file, 'a+') as f:
		aux = False
		i = 0
		for tweet_id in tweet_id_list:
			try:
				tweet = api.get_status(tweet_id)

				text = tweet.text
				author = tweet.author.id

				line = [w for w in text.split() if not w=='\n']
				result = ' '.join(line)

				x = {json_alter:{'text':result,'author':author}}
				y = json.dumps(x)

				f.write(y)
				f.write('\n')

				i = i + 1
				if aux:
					sys.stdout.write("\033[F")
				else:
					aux = True
				print ('Coleta: ' + str(i))
			except KeyboardInterrupt:
				print ('Processo Interrompido.')
				sys.exit()
			except:
				print (str(sys.exc_value[0]))
				aux = False
				continue

#-------------------------------------------------------------------------#

alters_list = []
json_alter = ""
def main():
	global alters_list
	global json_alter
	fonte_alters_list = os.listdir(fonte_alters)

	print ("Coletando Retweets:")

	for file in os.listdir(fonte_egos):

		ego = file.split(".dat")
		ego = ego[0]

		if (ego + '.json') in os.listdir(output):
			print ('#-----> Ego já coletado ou em coleta: ' + ego)
			continue

		print ('#-----> Ego: ' + ego)

		alters_list = read_ego_bin(fonte_egos+file)

		for alter in alters_list:
			json_alter = alter
			print ('#---> Alter ' + str(alter))

			if not (str(alter)+'.dat') in fonte_alters_list:
				print ('ALTER NAO TEM RETWEETS')
			else:
				tweet_id_list = read_alter_bin(fonte_alters+str(alter)+'.dat')
				collect_and_save(tweet_id_list, ego)

#-------------------------------------------------------------------------#

fonte_egos = "/home/amaury/dataset/n2/egos/bin/"
fonte_alters = "/home/amaury/dataset/n2/alters/bin/"
output = "/home/amaury/Lucas/n2/alters/"

#-------------------------------------------------------------------------#

formato = 'll' # Long para id do tweet e outro long para autor
timeline_struct = struct.Struct(formato) # Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#-------------------------------------------------------------------------#

#API Tweepy

#Autenticações
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

#Login na API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#-------------------------------------------------------------------------#
#Executa o método main
if __name__ == "__main__": main()
