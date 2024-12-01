


def parsear(texto: str):
    lista_esq = []
    lista_dir = []

    with open(texto, 'r') as text:
        for texto in text:
            esq, dir = map(int, texto.split())
            lista_esq.append(esq)
            lista_dir.append(dir)
    return lista_esq, lista_dir 

def distancia(lista_esquerda, lista_direita):
    lista_esquerda.sort()
    lista_direita.sort()
    listacombinada = 0

    for i, j in zip(lista_esquerda, lista_direita):
        listacombinada += abs(i - j)
    return listacombinada

input = 'texto.txt'

lista_esq, lista_dir = parsear(input)

key = distancia(lista_esq, lista_dir)

print(key)