import random
from termcolor import colored          # Se precisar instalar: "pip install termcolor"
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
    print(colored('       |=================================|', 'cyan'))
    print(colored('       | Bem vindo(a) ao Jogo dos países |', 'cyan'))
    print(colored('       |                                 |', 'cyan'))
    print(colored('       |     Seu objetivo é acertar      |', 'cyan'))
    print(colored('       |  um país sorteado pelo sistema  |', 'cyan'))
    print(colored('       |                                 |', 'cyan'))
    print(colored('       |          Boa Sorte!!            |', 'cyan'))
    print(colored('       |=================================|', 'cyan'))
    print()
    print(colored('|===============================================|', 'cyan'))
    print(colored('|                     Opções:                   |', 'cyan'))
    print(colored('|-----------------------------------------------|', 'cyan'))
    print(colored('| 1-Fazer um chute --> Digite o nome de um país |', 'cyan'))
    print(colored('| 2-Obter uma dica --> Digite "dica"            |', 'cyan'))
    print(colored('| 3-Desistir --------> Digite "desisto"         |', 'cyan'))
    print(colored('|===============================================|', 'cyan'))

    Pais_escolhido= sorteia_pais(Dados_normalizados)
    lista=[]
    dic={'cor':' Cores da bandeira: ', 'continente':'', 'area':'', 'pop':'', 'letra':' Letras da capital do país: '}
    chaves=list(dic.keys())
    lista_ja_escolhido=[]
    lista_de_tentativas=[]
    lista_de_dicas=[]
    lista_dics=[]
    restrita=[]
    lista_cores=[]
    letra=[]
    cor=[]
    Tentativas=20
    parar=False

    for i in Dados_normalizados[Pais_escolhido]['bandeira']:
        if Dados_normalizados[Pais_escolhido]['bandeira'][i]>0:
            if i != 'outras':
                lista_cores.append(i)

    for i in Dados_normalizados:
        pais= i
        lat1=Dados_normalizados[i]["geo"]["latitude"]
        lat2=Dados_normalizados[Pais_escolhido]["geo"]["latitude"]
        long1=Dados_normalizados[i]["geo"]["longitude"]
        long2=Dados_normalizados[Pais_escolhido]["geo"]["longitude"]
        distancia=haversine(EARTH_RADIUS, lat1, long1, lat2, long2)
        adiciona_em_ordem(pais, distancia, lista)

    while not parar:
        parar2=False

        if len(lista_de_tentativas)>0:
            print()
            print(colored('Distancias:    ', 'cyan'))
            print(colored('---------------------------------', 'cyan'))
            print('\n'.join(lista_ja_escolhido))
            print()

        if len(lista_dics)>0:
            print(colored('Dicas:', 'cyan'))
            print(colored('----------------------------------------------------------', 'cyan'))
            for i in lista_dics:
                if dic[i]==list:
                    print(dic[i][1:len(dic[i]-1)] )
                if dic[i]!=list:  
                    print(dic[i])
                print(colored('----------------------------------------------------------', 'cyan'))

        while not parar2:
            print()
            pais2=input("    De seu palpite:   ")
            print()
            pais2=pais2.lower()
            if pais2!='dica' and pais2!='desisto':
                if esta_na_lista(pais2, lista)==True:
                    parar2=True
                else:
                    print()
                    print("   O país citado infelizmente não se encontra em nosso banco de dados   ")
                    print()
            else:
                parar2=True

        if pais2!='dica' and pais2!='desisto':
            for i in lista:
                if pais2==i[0]:
                    distancia2=i[1]
            if len(str(distancia2))>3:
                x=str(distancia2)[:-3]+'.'+str(distancia2)[-3:]
            if len(str(distancia2))<=3:
                x=distancia2

            if distancia2==0:
                print()
                print(colored("   Parabéns, você acertou!!!   ", 'magenta'))
                print()
                quer_parar=input('   Deseja jogar novamente?   (s/n)  ')
                if quer_parar=='n':
                    parar_tudo=True
                parar=True  
            else:
                if len(lista_ja_escolhido)==0:
                    if distancia2>5000:
                        lista_ja_escolhido.append(colored(f'  {pais2} ------> {x} Km', 'red'))
                    if 2000<distancia2<=5000:
                        lista_ja_escolhido.append(colored(f'  {pais2} ------> {x} Km', 'yellow'))
                    if distancia2<=2000:
                        lista_ja_escolhido.append(colored(f'  {pais2} ------> {x} Km', 'green'))        
                    numeros.append(distancia2)

                else:
                    numeros.append(distancia2)
                    numeros.sort()
                    if distancia2>5000:
                        lista_ja_escolhido.insert(numeros.index(distancia2), colored(f'  {pais2} ------> {x} Km', 'red'))
                    if 2000<distancia2<=5000:
                        lista_ja_escolhido.insert(numeros.index(distancia2), colored(f'  {pais2} ------> {x} Km', 'yellow'))
                    if distancia2<=2000:
                        lista_ja_escolhido.insert(numeros.index(distancia2), colored(f'  {pais2} ------> {x} Km', 'green'))  

            if pais not in lista_de_tentativas:
                Tentativas-=1
                lista_de_tentativas.append(pais2)

            if distancia!=0:

                if 15<=Tentativas<=20:
                    print()
                    print (colored(f"   Você tem mais {Tentativas} tentativa(s)   ", 'green'))
                    print()
                if 5<Tentativas<15:
                    print()
                    print (colored(f"   Você tem mais {Tentativas} tentativa(s)   ", 'yellow'))
                    print()
                if 0<=Tentativas<=5:
                    print()
                    print (colored(f"   Você tem mais {Tentativas} tentativa(s)   ", 'red'))
                    print()

        if pais2 == 'dica':

            print()
            print()
            print()
            print(colored('|=================================|', 'cyan'))
            print(colored('| Escolha uma das opções a baixo  |', 'cyan'))
            print(colored('|---------------------------------|', 'cyan'))

            if Tentativas>4:
                print(colored('|    Cores da bandeira do país    |', 'cyan'))
                print(colored('|          Digite:"cor"           |', 'cyan'))
                print(colored('|        Custo = 4 tentativas     |', 'cyan'))
            else:
                print(colored('|                                 |', 'cyan'))
                print(colored('|                                 |', 'cyan'))
                print(colored('|                                 |', 'cyan'))
            print(colored('|---------------------------------|', 'cyan'))
            if Tentativas>3:
                print(colored('|      Letras de sua capital      |', 'cyan'))
                print(colored('|         Digite:"letra"          |', 'cyan'))
                print(colored('|        Custo = 3 tentativas     |', 'cyan'))
            else:
                print(colored('|                                 |', 'cyan'))
                print(colored('|                                 |', 'cyan'))
                print(colored('|                                 |', 'cyan'))
            print(colored('|---------------------------------|', 'cyan'))
            if Tentativas>6 and 'area' not in lista_de_dicas:
                print(colored('|              Área               |', 'cyan'))
                print(colored('|          Digite:"area"          |', 'cyan'))
                print(colored('|        Custo = 6 tentativas     |', 'cyan'))
            else:
                print(colored('|                                 |', 'cyan'))
                print(colored('|                                 |', 'cyan'))
                print(colored('|                                 |', 'cyan'))            
            print(colored('|---------------------------------|', 'cyan'))
            if Tentativas>5 and 'pop' not in lista_de_dicas:
                print(colored('|           População             |', 'cyan'))
                print(colored('|          Digite:"pop"           |', 'cyan'))
                print(colored('|        Custo = 5 tentativas     |', 'cyan'))
            else:
                print(colored('|                                 |', 'cyan'))
                print(colored('|                                 |', 'cyan'))
                print(colored('|                                 |', 'cyan'))            
            print(colored('|---------------------------------|', 'cyan'))
            if Tentativas>7 and 'continente' not in lista_de_dicas:
                print(colored('|           Continente            |', 'cyan'))
                print(colored('|       Digite:"continente"       |', 'cyan'))
                print(colored('|       Custo = 7 tentativas      |', 'cyan'))
            else:
                print(colored('|                                 |', 'cyan'))
                print(colored('|                                 |', 'cyan'))
                print(colored('|                                 |', 'cyan'))
            print(colored('|=================================|', 'cyan'))
            print()
            print()
            parar3=False

            while not parar3:
                print()
                print()
                dica=input("     Qual dica você escolheu?     ")
                print()

                if dica in lista_dicas:
                    parar3=True
                    break

                else:
                    print(' Esta dica não existe')   

            if dica=='cor':
                
                if Tentativas <= 4:
                    print()
                    print(colored(' Você não possui tentativas sulficientes para comprar essa dica', 'red'))
                    print()

                else:
                    if len(lista_cores)>0:
                        x=random.choice(lista_cores)
                        print()
                        b=dic['cor']+str(x)+', '
                        dic['cor'] = b
                        print()
                        lista_cores.remove(x)
                        if 'cor' not in lista_dics:
                            lista_dics.append('cor')
                        Tentativas-= 4
                    else:
                        print(colored(' As cores principais da bandeira do país já foram reveladas ', 'red'))


            if dica=='letra':

                if Tentativas <=  3 :
                    print()
                    print(colored(' Você não possui tentativas sulficientes para comprar essa dica ', 'red'))
                    print()

                else:   
                    if len(Dados_normalizados[Pais_escolhido]["capital"])==len(restrita):
                        print()
                        print(' Todas as letras da já foram reveladas ')
                        print()
                    else:
                        x=sorteia_letra(Dados_normalizados[Pais_escolhido]["capital"], restrita)
                        print()
                        b=dic['letra']+str(x)+', '
                        dic['letra'] = b
                        print()
                        restrita.append(x)
                        if 'letra' not in lista_dics:
                            lista_dics.append('letra')
                        Tentativas-= 3

            if dica=='pop':

                if 'pop' in lista_de_dicas:
                    print()
                    print(colored(' Esta dica já foi previamente escolhida', 'red'))
                    print()

                else:
                    lista_de_dicas.append('pop')

                    if Tentativas <= 5  :
                        print()
                        print(colored(' Você não possui tentativas sulficientes para comprar essa dica', 'red'))
                        print()

                    else:
                        print()
                        b=' O país tem {} habitantes'.format(Dados_normalizados[Pais_escolhido]['populacao'])
                        dic['pop']=b
                        print()
                        lista_dics.append('pop')
                        Tentativas-= 5

            if dica=='area':

                if 'area' in lista_de_dicas:
                    print()
                    print(colored(' Esta dica já foi previamente escolhida', 'red'))
                    print()

                else:
                    lista_de_dicas.append('area')

                    if Tentativas <=  6 :
                        print()
                        print(colored(' Você não possui tentativas sulficientes para comprar essa dica', 'red'))
                        print()

                    else:
                        print()
                        b=' O país tem uma área de {} metros quadrados'.format(Dados_normalizados[Pais_escolhido]['area'])
                        dic['area']=b
                        print()
                        lista_dics.append('area')
                        Tentativas-= 6

            if dica=='continente':

                if 'continente' in lista_de_dicas:
                    print()
                    print(colored(' Esta dica já foi previamente escolhida', 'red'))
                    print()

                else:
                    lista_de_dicas.append('continente')

                    if Tentativas <=  7 :
                        print()
                        print(colored(' Você não possui tentativas sulficientes para comprar essa dica', 'red'))
                        print()

                    else:
                        print()
                        b=' É um país da {}'.format(Dados_normalizados[Pais_escolhido]['continente'])
                        dic['continente']=b
                        print()
                        lista_dics.append('continente')
                        Tentativas-= 7

            if Tentativas!=0:

                if 15<=Tentativas<=20:
                    print()
                    print (colored(f"   Você tem mais {Tentativas} tentativa(s)   ", 'green'))
                    print()

                if 5<Tentativas<15:
                    print()
                    print (colored(f"   Você tem mais {Tentativas} tentativa(s)   ", 'yellow'))
                    print()

                if 0<=Tentativas<=5:
                    print()
                    print (colored(f"   Você tem mais {Tentativas} tentativa(s)   ", 'red'))
                    print()

        if pais2 == 'desisto':

            certeza=input('      Tem certeza que deseja desistir?   (s/n)   ')

            if certeza == 's':
                print()
                print(f'     O país correto era :{Pais_escolhido}')
                print()

                quer_parar=input('     Deseja jogar novamente?   (s/n)  ')

                if quer_parar=='n':
                    print()
                    print("     Obrigado por jogar!!     ")
                    print()
                    print("        Até a proxima     ")
                    print()
                    parar_tudo=True
                parar=True

        if Tentativas==0:

            print()
            print(colored("     Suas tentativas se esgotaram     ", 'red'))
            print()
            print(colored(f'     O país correto era :{Pais_escolhido}     ', 'cyan'))
            print()
            parar=True
            quer_parar=input('     Deseja jogar novamente?   (s/n)  ')

            if quer_parar=='n':
                print()
                print("     Obrigado por jogar!!     ")
                print()
                print("        Até a proxima     ")
                print()
                parar_tudo=True