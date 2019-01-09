def new_indice(lines):
    indice = {}
    contador = 0
    for l in lines:
        for w in l.split():
            if not w in indice.keys():
                indice[w] = contador
                contador += 1

def main():
    import os
    folder = "egos/"
    for doc in os.listdir(folder):
        print("\n\n--> " + doc)

        file = folder + doc
        f = open(file, 'r')

        lines = f.readlines()

        indice = {}  #mapeamento do termo para inteiro
        indice_ocorrencia = {}  #tweets em que o termo aparece
        contador = 0

        for index, l in enumerate(lines):
            for w in l.split():
                if not w in indice.keys():
                    indice[w] = contador
                    contador += 1
                    indice_ocorrencia[indice[w]] = [index]
                else:
                    indice_ocorrencia[indice[w]].append(index)
# -------------------------------------------------------------------------#
# Executa o metodo main
if __name__ == "__main__": main()