def contagem_interseccao(a, b):
    s = set(a)
    return len(s.intersection(b))

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
    import numpy as np
    import json
    folder = "Documentos Finais/"
    output_matriz = "Matrizes de Coocorrencia/"
    output_indice = "Indices de Termos/"
    for doc in os.listdir(folder):
        print("--> " + doc)

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

        #Salvando indice Termo-Inteiro
        file = output_indice + (doc.split('.txt')[0]) + '.json'
        output = open(file, 'w+')
        out = json.dumps(indice)
        output.write(out)
        output.close()

        #Montando e salvando matriz de coocorrencia
        file = output_matriz + doc
        output = open(file, 'a+')

        B = np.zeros((contador,contador), dtype=np.int_)

        for i in range(0,contador):
            for j in range(0,contador):
                B[i][j] = contagem_interseccao(indice_ocorrencia[i], indice_ocorrencia[j])
                output.write(str(B[i][j]) + ' ')
            output.write('\n')

        output.close()


# -------------------------------------------------------------------------#
# Executa o metodo main
if __name__ == "__main__": main()