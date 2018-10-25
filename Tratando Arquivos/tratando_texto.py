#Tokenize sentence with NLTK; Removing special characters and stop-words.
def tokenize(sentence):
	from nltk.corpus import stopwords
	from nltk.tokenize import RegexpTokenizer
	#import nltk	
	#nltk.download('punkt')
	#nltk.download('stopwords')

	stop_words = set(stopwords.words('english'))
	#stop_words = set(stopwords.words('portuguese'))

	tokenizer = RegexpTokenizer(r'\w+')
	sentence = tokenizer.tokenize(sentence)

	tokens = [w for w in sentence if not w in stop_words]

	return tokens

#-------------------------------------------------------------------------#

def remove_links(sentence):

	no_links = ""
	for w in sentence.split():
		if not "http" in w:
			no_links += str(w + " ")

	return no_links

#-------------------------------------------------------------------------#

def save_tokens(id, sentence, rem_links = False):
	output = "/home/amaury/Lucas/n2/textos_tradados/egos/" # Altere para a pasta de output
	if remove_links:
		sentence = remove_links(sentence)

	tokens = tokenize(sentence)
	if len(tokens) == 0:
		return

	doc_save = output + id + '.txt'
	with open(doc_save, 'a+') as f:
		for w in tokens:
			f.write(str(w + " "))
		f.write(str("\n"))

#-------------------------------------------------------------------------#

def main():
	import os
	folder = "/home/amaury/Lucas/n2/egos/" # Altere para a pasta contendo os arquivos com os tweets de cada rede ego.
	for doc in os.listdir(folder):
		print("--> " + doc)

		id = doc.split(".txt")
		id = id[0]

		file = folder + doc
		with open(file, 'r', encoding='utf-8') as f:
			for line in f:
				save_tokens(id, line, rem_links = True)

#-------------------------------------------------------------------------#
#Executa o método main
if __name__ == "__main__": main()
