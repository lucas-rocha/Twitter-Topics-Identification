#Tokenize sentence with NLTK; Removing special characters and stop-words.
def tokenize(sentence):
    from nltk.corpus import stopwords
    from nltk.tokenize import RegexpTokenizer
    #nltk.download('punkt')
    #nltk.download('stopwords')

    stop_words = set(stopwords.words('english'))

    tokenizer = RegexpTokenizer(r'\w+')
    sentence = tokenizer.tokenize(sentence)

    tokens = [w for w in sentence if not w in stop_words]

    return tokens

#------------------------#

def save_tokens(sentence):
    tokens = tokenize(sentence)

    file = open('SeaNMF-master/data/data.txt', 'a+')
    for w in tokens:
        file.write(str(w + " "))
    file.write(str("\n"))
    file.close()

#-----------------------#

file = open('Tratando Arquivos/data.txt', 'r')
i = 0
for line in file:
    i = i + 1
    save_tokens(line)
    print("Text " + str(i))
file.close()
