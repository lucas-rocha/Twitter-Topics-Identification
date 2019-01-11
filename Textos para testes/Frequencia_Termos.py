from operator import itemgetter
from nltk.corpus import stopwords
from stopwords import stop_words

def stopwords(line):
    words = line.split()
    wordsFiltered = []

    for w in words:
        if w not in stop_words:
            wordsFiltered.append(w)

    return wordsFiltered


def contagem(lines, t):
    cont = 0
    for line in lines:
        l = line.split()
        for termo in l[1:]:
            if termo == t:
                cont+=1
                break

    return cont

def main():
    import os
    folder = "egos/"
    for doc in os.listdir(folder):
        print("\n\n--> " + doc)

        file = folder + doc
        f = open(file, 'r')

        lines = f.readlines()

        termos = {}

        for line in lines:
            l = line[len(line.split()[0])+1:]
            tweet = stopwords(l)
            for termo in tweet:
                if not termo in termos.keys():
                    termos[termo] = contagem(lines, termo)

        print(sorted(termos.items(), key = itemgetter(1), reverse=True))
        print(len(termos))
        aux = 0
        for t in termos:
            if termos[t] > 3:
                aux += 1
        print(aux)

# -------------------------------------------------------------------------#
# Executa o metodo main
if __name__ == "__main__": main()
