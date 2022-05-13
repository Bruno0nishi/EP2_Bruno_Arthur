import random
from Funções import sorteia_pais
from Funções import normaliza
from Funções import haversine
from Funções import adiciona_em_ordem
from Funções import esta_na_lista
from Funções import sorteia_letra
from basededados import EARTH_RADIUS
from basededados import DADOS

Dados_normalizados= normaliza(DADOS)

lista_dicas=['continente', 'cor', 'area', 'pop', 'letra']
numeros=[]
parar_tudo=False

while not parar_tudo:

    print()
    print('|=================================|')
    print('| Bem vindo(a) ao Jogo dos países |')
    print('|                                 |')
    print('|  Seu objetivo vai ser acertar   |')
    print('| um país sortesado pelo sistema  |')
    print('|=================================|')