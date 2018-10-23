import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
#reload(sys)
sys.setdefaultencoding('utf-8')

##########################################################################################

formato = 'll' # Long para id do tweet e outro long para autor
timeline_struct = struct.Struct(formato) # Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

##########################################################################################

fonte_egos = "/home/amaury/dataset/n2/egos/bin/"
fonte_alters = "/home/amaury/dataset/n2/alters/bin/"
output = "/home/amaury/Lucas/n2/alters/"

############################################################################################

def read_ego_bin(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		alters_list = []
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			retweet, user = timeline_struct.unpack(buffer) #Lucas aqui você consegue o id do retweet e o id do autor... eu salvei em json só o id do autor. É so usar a informação que está na variável "retweet" também.
			alters_list.append(user)
	return authors_list

##########################################################################################

def read_alter_bin(file):
	global alters_list
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		tweet_id_list = []
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			retweet, user = timeline_struct.unpack(buffer) #Lucas aqui você consegue o id do retweet e o id do autor... eu salvei em json só o id do autor. É so usar a informação que está na variável "retweet" também.
			
			if user in alters_list:
				tweet_id_list.append(retweet)
	return tweet_id_list

##########################################################################################

def collect(tweet_id_list):
	tweet_list = []

	for tweet in tweet_id_list:
		print()

##########################################################################################

def saving_file(tweet_list, ego):
	file = output + ego + '.txt'
	with open(file, 'w+') as f:
		for tweet in tweet_list:
			f.write(tweet)

##########################################################################################

alters_list = []
def main():
	global alters_list
	i = 0 # egos com retweets de alters coletados
	print ("Coletando Retweets:")

	for file in os.listdir(fonte_egos):
		i+=1
		print ('---> Ego ' + i + ':')

		ego = file.split(".dat")
		ego = ego[0]

		alters_list = read_ego_bin(fonte_egos+file)
		
		for alter in alters_list:
			print ('-> Alter ' + alter + ':')
			
			tweet_id_list = read_alter_bin(fonte_alters+alter+'.dat')
			for tweet in tweet_id_list:
				print (tweet)
			#tweet_list = collect(tweet_id_list)
			#saving_file(tweet_list, ego)



