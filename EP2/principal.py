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
    print(colored('|=================================|', 'cyan'))
    print(colored('| Bem vindo(a) ao Jogo dos países |', 'cyan'))
    print(colored('|                                 |', 'cyan'))
    print(colored('|  Seu objetivo vai ser acertar   |', 'cyan'))
    print(colored('| um país sortesado pelo sistema  |', 'cyan'))
    print(colored('|=================================|', 'cyan'))

    Pais_escolhido= sorteia_pais(Dados_normalizados)
    lista=[]
    lista_de_tentativas=[]
    lista_de_dicas=[]
    lista_cores=[]
    Tentativas=20
    parar=False

    for i in Dados_normalizados[Pais_escolhido]['bandeira']:
        if Dados_normalizados[Pais_escolhido]['bandeira'][i]>0:
            if i != 'outros':
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

        print()
        print()
        print()
        print()
        print('|=================================|')
        print('|                                 |')
        print('|    1  ->  Fazer um chute        |')
        print('|    2  ->  Obter uma dica        |')
        print('|    3  ->  Desistir              |')
        print('|                                 |')
        print('|=================================|')
        print()
        print()
        print()
        Tenta_ou_Compra=input("  Pressione 1 para fazer um chute, 2 para obter uma dica e 3 para desistir  ")
        print()

        if Tenta_ou_Compra == '1':
            parar2=False


            while not parar2:
                print()
                pais2=input("   Digite um país:   ")
                print()
                pais2=pais2.lower()
                if esta_na_lista(pais2, lista)==True:
                    parar2=True
                else:
                    print()
                    print("   O país citado infelizmente não se encontra em nosso banco de dados   ")
                    print()


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
                quer_parar=input('     Deseja jogar novamente?   (s/n)  ')
                if quer_parar=='n':
                    parar_tudo=True
                parar=True   

            if distancia2!=0:
                print()
                print(x)
                print()


            if pais not in lista_de_tentativas:
                Tentativas-=1
                lista_de_tentativas.append(pais2)


            if distancia!=0:

                if 15<=Tentativas<=20:
                    print()
                    print (f"   Você tem mais {Tentativas} tentativa(s)   ")
                    print()


        if Tenta_ou_Compra == '2':

            print()
            print()
            print()
            print('|=================================|')
            print('| Escolha uma das opções a baixo  |')
            print('|---------------------------------|')

            if Tentativas>4:
                print('|    Cores da bandeira do país    |')
                print('|          Digite:"cor"           |')
                print('|        Custo = 4 tentativas     |')
            else:
                print('|                                 |')
                print('|                                 |')
                print('|                                 |')
            print('|---------------------------------|')
            if Tentativas>3:
                print('|     Letras de sua capital       |')
                print('|         Digite:"letra"          |')
                print('|        Custo = 3 tentativas     |')
            else:
                print('|                                 |')
                print('|                                 |')
                print('|                                 |')
            print('|---------------------------------|')
            if Tentativas>6 and 'area' not in lista_de_dicas:
                print('|              Área               |')
                print('|          Digite:"area"          |')
                print('|        Custo = 6 tentativas     |')
            else:
                print('|                                 |')
                print('|                                 |')
                print('|                                 |')            
            print('|---------------------------------|')
            if Tentativas>5 and 'pop' not in lista_de_dicas:
                print('|           População             |')
                print('|          Digite:"pop"           |')
                print('|        Custo = 5 tentativas     |')
            else:
                print('|                                 |')
                print('|                                 |')
                print('|                                 |')            
            print('|---------------------------------|')
            if Tentativas>7 and 'continente' not in lista_de_dicas:
                print('|           Continente            |')
                print('|       Digite:"continente"       |')
                print('|        Custo = 7 tentativas     |')
            else:
                print('|                                 |')
                print('|                                 |')
                print('|                                 |')
            print('|=================================|')
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


            if dica =='cor':
                x=random.choice(lista_cores)     
                print (f'Uma das cores é : {x}') 
                lista_cores.remove(x)
                    
        if Tenta_ou_Compra == '3':

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
            print("     Suas tentativas se esgotaram     ")
            print()
            print(f'   O país correto era :{Pais_escolhido}     ')
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


