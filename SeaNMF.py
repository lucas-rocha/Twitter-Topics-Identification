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


sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."
tokens = tokenize(sentence)

file = open('SeaNMF-master/data/data.txt', 'w+')
for w in tokens:
    file.write(str(w + " "))
file.close()
