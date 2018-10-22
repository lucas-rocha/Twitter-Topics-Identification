#Tokenize sentence with NLTK; Removing special characters and stop-words.
def tokenize(sentence):
    from nltk.corpus import stopwords
    from nltk.tokenize import RegexpTokenizer
    #nltk.download('punkt')
    #nltk.download('stopwords')

    stop_words = set(stopwords.words('english'))
    #stop_words = set(stopwords.words('portuguese'))

    tokenizer = RegexpTokenizer(r'\w+')
    sentence = tokenizer.tokenize(sentence)

    tokens = [w for w in sentence if not w in stop_words]

    return tokens

#------------------------#

def remove_links(sentence):

    no_links = ""
    for w in sentence.split():
        if not "http" in w:
            no_links += str(w + " ")

    return no_links

#------------------------#

def save_tokens(sentence, rem_links = False):

    if remove_links:
        sentence = remove_links(sentence)

    tokens = tokenize(sentence)
    if len(tokens)==0:
        return

    global id
    doc_save = 'timelines_tratadas/' + id + '.txt'
    file = open(doc_save, 'a+')
    for w in tokens:
        file.write(str(w + " "))
    file.write(str("\n"))
    file.close()

#------------------------#

id = '5781452'
doc = 'timelines/' + id + '.txt'
file = open(doc, 'r', encoding='utf-8')

i = 0
for line in file:
    i = i + 1
    save_tokens(line, rem_links = True)
    print("Text " + str(i))
file.close()
