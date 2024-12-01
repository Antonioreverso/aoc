def parsear(texto: str):
    lista_esq = []
    lista_dir = []

    with open(texto, 'r') as text:
        for texto in text:
            esq, dir = map(int, texto.split())
            lista_esq.append(esq)
            lista_dir.append(dir)
    return lista_esq, lista_dir

def similar(lista_esquerda, lista_direita):
    total = 0

    for i in lista_esquerda:
        aparece = lista_direita.count(i)
        total += i*aparece
    return total

input = 'texto.txt'

lista_esq, lista_dir = parsear(input)

key = similar(lista_esq, lista_dir)

print(key)