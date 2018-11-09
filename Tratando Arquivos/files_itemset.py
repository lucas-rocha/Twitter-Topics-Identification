# -*- coding: utf-8 -*-
# -> Escrito para python 2 <- #
import datetime, sys, time, os, os.path, shutil, time, struct, random
import numpy as np
reload(sys)
sys.setdefaultencoding('utf-8')

#-------------------------------------------------------------------------#

def read_alter_bin(file):
	global alters_list

	with open(file, 'r') as f:
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		tweet_id_list = []
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			retweet, user = timeline_struct.unpack(buffer)

			if user in alters_list:
				tweet_id_list.append(retweet)
	return tweet_id_list

#-------------------------------------------------------------------------#

data = {}
alters_list = []
def main():
	global data
	global alters_list
	fonte_alters_list = os.listdir(fonte_alters)

	with open(fonte_ego, 'r') as f:

		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			retweet, user = timeline_struct.unpack(buffer)
			if not user in alters_list:
				alters_list.append(user)

		for alter in alters_list:
			print ('#---> Alter ' + str(alter))

			if not (str(alter)+'.dat') in fonte_alters_list:
				print ('ALTER NAO TEM RETWEETS')
			else:
				tweet_id_list = read_alter_bin(fonte_alters+str(alter)+'.dat')
				if len(tweet_id_list) > 0:
					data[alter] = np.sort(tweet_id_list)

	alters = np.sort(data.keys())
	with open(output_tweets, 'a+') as f:
		for a in alters:
			tweet_list = data[a]
			for t in tweet_list:
				f.write(str(t) + " ")
			f.write("\n")

	with open(output_users, 'a+') as f:
		for a in alters:
			f.write(str(a) + '\n')

#-------------------------------------------------------------------------#

fonte_ego = "/home/amaury/dataset/n2/egos/bin/1525391.dat"
fonte_alters = "/home/amaury/dataset/n2/alters/bin/"
output_tweets = "/home/amaury/Downloads/tweets.txt"
output_users = "/home/amaury/Downloads/users.txt"

#-------------------------------------------------------------------------#

formato = 'll' # Long para id do tweet e outro long para autor
timeline_struct = struct.Struct(formato) # Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#-------------------------------------------------------------------------#
#Executa o método main
if __name__ == "__main__": main()
