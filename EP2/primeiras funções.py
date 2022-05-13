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