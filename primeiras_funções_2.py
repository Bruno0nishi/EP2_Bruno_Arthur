import random

def adiciona_em_ordem(pais, distancia, lista):
    pais_na_lista=False
    x=0
    for i in lista:
        if i[0]==pais:
            pais_na_lista=True
            break
    if pais_na_lista==False:
        for x in range(len(lista)):
            if lista[x][1]>distancia:
                break
            x+=1
        lista.insert(x, [pais, distancia])
    return lista

def esta_na_lista(pais, lista):
    pais_na_lista=False
    for i in lista:
        if i[0]==pais:
            pais_na_lista=True
    return pais_na_lista

def sorteia_letra(palavra, restrita):
    caracter=['.', ',', '-', ';', ' ']
    lista=[]
    for i in list(palavra.lower()):
        if i not in lista:
            if i not in restrita and i not in caracter :
                lista.append(i)
    if len(lista)==0:
        return ''
    else:
        return random.choice(lista)