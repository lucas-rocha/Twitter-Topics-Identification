# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##	2017-08-06
##		Status - Versão 1 - Faz leitura do binário e salva apenas o ID DOS AUTORES de RETWEETS do EGO em formato JSON.
##								Cria um ÙNICO ARQUIVO com todos os alters...
##								ARQUIVOS GERADOS PARA SEREM USADOS NO mytweetf0rm
## 
######################################################################################################################################################################

################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_bin(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		authors_list = []
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			retweet, user = timeline_struct.unpack(buffer) #Lucas aqui você consegue o id do retweet e o id do autor... eu salvei em json só o id do autor. É so usar a informação que está na variável "retweet" também.
			authors_list.append(user)
	return authors_list

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	i = 0		# egos convertidos
	print ("Convertendo egos:")
	alters_set = set()

	for file in os.listdir(fonte):
		i+=1
		authors_list = read_arq_bin(fonte+file)
		ego = file.split(".dat")
		ego = long(ego[0])
		if authors_list:
			print i
			for user in authors_list:
				alters_set.add(user)

	alters_list = list(alters_set)	

	# Teste (Lucas)
	for alter in alters_list:
		print alter

	#with open(output, 'w') as f:
	#	json.dump(alters_list, f)


#Teste de impressão dos alters para verificar integridade da conversão.
	#with open(output, 'r') as f:	
	#	alters = json.load(f)
	#for alter in alters:
	#	print alter			
	print("######################################################################")
	print("Coleta finalizada!")
	print("######################################################################\n")
#####################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
fonte = "/home/amaury/dataset/n2/egos/bin/"
output = "/home/amaury/dataset/n2/egos/n2_500_egos_retweets_alters_ids.json"

formato = 'll'				##################################################################  Long para id do tweet e outro long para autor
timeline_struct = struct.Struct(formato) ################################################# Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#Executa o método main
if __name__ == "__main__": main()
