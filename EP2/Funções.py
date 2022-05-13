import random
import math

def normaliza(entrada):
    saida={}
    for i in entrada:
        for n in entrada[i]:
            entrada[i][n]['continente']=i
            saida[n]=entrada[i][n]
    return saida

def sorteia_pais(entrada):
    lista=list(entrada.keys())
    return random.choice(lista)

def haversine(raio, lat1, long1, lat2, long2):
    primeira_etapa=((math.sin(math.radians((lat2-lat1)/2)))**2)
    segunda_etapa=math.cos(math.radians(lat1))
    terceira_etapa=math.cos(math.radians(lat2))
    quarta_etapa=((math.sin((math.radians((long2-long1)/2))))**2)
    distancia=2*raio*math.asin((primeira_etapa + segunda_etapa * terceira_etapa * quarta_etapa)**(1/2))
    return  int(distancia)

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