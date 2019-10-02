import PyUrnaGravador
import os
import sys
import platform
import time
from io import StringIO
sair =True


def CadastrarCadidatos(ListaCadidadtos):
    gravar = open("candidatos.txt", "a+")
    gravar.write(ListaCadidadtos)
    gravar.write("\n")
    gravar.close()

def recuperaCadidatos():
    gravar = open("candidatos.txt", "r+")
    lista = ""
    for k in gravar.readlines():
        lista = lista + k + '\n'
    gravar.close()
    return lista


def ContagemEleitores():
    pegar = open("eleitores.txt", "r")
    cont = 0
    for k in pegar:
      k = k.split(";")
      if(k[2] == "True"):
        cont+=1
    pegar.close()
    return cont

def ContagemEleitoresnao():
    pegar = open("eleitores.txt", "r")
    cont = 0
    for k in pegar:
      k = k.split(";")
      if(k[2] == "False"):
         cont+=1
    pegar.close()
    return cont


def LimparTela ():
    sistema = platform.system()
    if(sistema == 'Windows'):
       return  os.system('cls')
    else:
        return os.system('clear')


def MenuAdmin (list):
    lista = open('eleitores.txt', 'r+')
    cont = int(list[1])
    ok = lista.readlines()
    ok = ok[cont]
    ok = ok.split(";")
    print('''
BEM VINDO %s A URNA ELETRÔNICA 
VOCÊ TEM PERMISSÃO ADMINISTRADOR
    \n \n'''%(ok[1]))
    print("--------------------------------------")
    op = input('''1) Cadastrar eleitor; 
2) Listar eleitores; 
3) Alterar dados de eleitor; 
4) Cadastrar candidato; 
5) Listar candidatos; 
6) Alterar candidato; 
7) Registrar voto; 
8) Consultar votos obtidos por candidato;
9) Consultar número de eleitores que já votaram; 
10) Consultar número de eleitores que ainda não votaram; 
11)Sair.\n''')

    if("1" == op):
        eleitor = input("Digite o numero;nome;se voltou ou n;nivel de permissão a ou b").lower()
        PyUrnaGravador.gravaEleitores(eleitor)
        print("Candidato cadastrado com sucesso!!!")
        print("Votando ao menu anterior...")
        time.sleep(3)
        LimparTela()
    elif("2" == op):
         print("Listando eleitores cadastrados: \n")
         print(PyUrnaGravador.recuperaEleitores())
         time.sleep(8)
         LimparTela()
    elif("3" == op):
        ListaEleitores = open("eleitores.txt","r")
        conta = 0
        salva = ""
        print("Modificando dados do eleitor")
        print("Digite o numero do matricula do eleitor que deseja mudar")
        matri = input()
        for k in ListaEleitores.readlines():
          if(matri in k):
             print("Entrou")
             salva = conta
          conta+=1
        print(salva)
        if(salva!=""):
            print("Eleitor encontrado!!")
            print("Digite as novas informações sobre ele: nome;se votou True ou não False;nivel de permicao")
            novo = input()
            nova = matri + "; "+ novo + "\n"
            buffer = StringIO()
            with open('eleitores.txt', 'r') as stream:
                for index, line in enumerate(stream):
                    buffer.write(nova if index == salva else line)
            with open('eleitores.txt', 'w') as stream:
                stream.write(buffer.getvalue())
            print("Modificado com sucesso!!!")
            print("Votando ao menu anterior...")
            time.sleep(3)
            LimparTela()
        else:
            print("Eleitor não encontrado!!!")
            print("Votando ao menu anterior...")
            time.sleep(3)
            LimparTela()
    elif("4" == op):
        cadidato = input("Digite o numero;nome;partido do Candidato").lower()
        CadastrarCadidatos(cadidato)
        print("Candidato cadastrado com sucesso!!!")
        print("Votando ao menu anterior...")
        time.sleep(3)
        LimparTela()
    elif("5" == op):
        print("Listando cadindatos cadastrados: \n")
        print(recuperaCadidatos())
        time.sleep(8)
        LimparTela()
    elif("6" == op):
        ListaCandidato = open("candidatos.txt", "r")
        conta = 0
        salva =""
        print("Modificando dados dos cadidatos")
        print("Digite o numero do cadidadto ")
        matri = input()
        for k in ListaCandidato.readlines():
          if (matri in k):
             salva = conta
          conta += 1
        if (salva != ""):
            print("Candidato encontrado!!")
            print("Digite as novas informações sobre ele: numero;nome;partido")
            novo = input()
            nova = novo
            buffer = StringIO()
            with open('candidatos.txt', 'r') as stream:
                for index, line in enumerate(stream):
                    buffer.write(nova+"\n" if index == salva else line)
            with open('candidatos.txt', 'w') as stream:
                stream.write(buffer.getvalue())
            print("Modificado com sucesso!!!")
            print("Votando ao menu anterior...")
            time.sleep(3)
            LimparTela()
        else:
            print("Cadidato não encontrado!!!")
            print("Votando ao menu anterior...")
            time.sleep(3)
            LimparTela()
    elif("7" == op):
        if (ok[2] == 'False'):
            nome=''
            votoS =''
            voto = input("Digite o numero do seu candidato:  OBS: Se for Branco digite branco e se for Nulo digite nulo").upper()
            candidatos = open("candidatos.txt", "r")
            for i in candidatos.readlines():
                i = i.split(";")
                if(i[0] == str(voto)):
                    nome = i[1]
            if(voto == "BRANCO" or voto == "NULO"):
                votoS = input("Confirmar seu voto no %s S/N?" % (voto)).upper()
            else:
                votoS = input("Confirmar seu voto no %s %s S/N?" % (nome,voto)).upper()
            if (votoS == "S"):
                listavoto = open("votos.txt", "a+")
                eleitores = open("eleitores.txt", "a+")
                listavoto.write(str(voto)+"\n")
                buffer = StringIO()
                nova = ok[0] + ";" + ok[1] + ";" + "True" + ";" + ok[3]
                with open('eleitores.txt', 'r') as stream:
                    for index, line in enumerate(stream):
                        buffer.write(nova if index == cont else line)
                with open('eleitores.txt', 'w') as stream:
                    stream.write(buffer.getvalue())
                print("Aguarde!! Estamos processando seu voto")
                time.sleep(2)
                print("Voto confirmado com sucesso")
                time.sleep(2)
                LimparTela()
            else:
                print("Renciando urna....")
                time.sleep(3)
                return False
        elif (ok[2] == 'True'):
            print("\nVocê ja votou, não pode votar duas vezes :(")
            print("\nVotando ao menu anterior, aguarde!!!")
            time.sleep(4)
            LimparTela()
    elif("8" == op):
        try:
            lista = open("votos.txt", "r")
            votoagr = lista.readlines()
            lista2 = open("candidatos.txt", "r")
            for k in lista2.readlines():
                cont2 = 0
                k = k.split(";")
                for j in votoagr:
                    if(k[0] in j):
                        cont2+=1
                print("O candidato do número %s tirou %d votos" %(k[0],cont2))
            print("Votando ao menu anterior...")
            time.sleep(6)
        except:
             print(" ")
    elif("9" == op):
        print("numero de eleitores que ja votaram:")
        print("Temos o total de ", ContagemEleitores()  )
        time.sleep(6)
        LimparTela()
    elif("10" == op):
        print("Numero de eleiores que ainda não votaram:")
        print("Temos o total de ", ContagemEleitoresnao())
        time.sleep(6)
        LimparTela()
    elif("11" == op):
        print("Encerrando conexao com servidor....")
        time.sleep(5)
        sys.exit()
    else:
        print("Opção invalida")


def MenuUsuario(list):
    lista = open('eleitores.txt', 'r')
    cont = int(list[1])
    ok = lista.readlines()
    ok = ok[cont]
    ok = ok.split(";")
    print('''
    BEM VINDO %s A URNA ELETRÔNICA  
    ELEITOR
        \n \n''' % (ok[1]))
    op = input('''1) Registrar voto
2) Sair\n''')
    if("1" == op and ok[2] == 'False'):
        votoS =''
        voto = input("Digite o numero do seu candidato:  OBS: Se for Branco digite branco e se for Nulo digite nulo").upper()
        candidatos = open("candidatos.txt", "r")
        for i in candidatos.readlines():
            i = i.split(";")
            if (i[0] == str(voto)):
                nome = i[1]
        if (voto == "BRANCO" or voto == "NULO"):
            votoS = input("Confirmar seu voto no %s S/N?" % (voto)).upper()
        else:
            votoS = input("Confirmar seu voto no %s %s S/N?" % (nome, voto)).upper()
        if(votoS == "S"):
            listavoto = open("votos.txt", "a+")
            eleitores = open("eleitores.txt", "a+")
            listavoto.write(str(voto)+"\n")
            buffer = StringIO()
            nova= ok[0] + ";" +ok[1] + ";" + "True" + ";" + ok[3]
            with open('eleitores.txt', 'r') as stream:
                for index, line in enumerate(stream):
                    buffer.write( nova if index == cont else line)
            with open('eleitores.txt', 'w') as stream:
                stream.write(buffer.getvalue())
            print("Aguarde!! Estamos processando seu voto")
            time.sleep(2)
            print("Voto confirmado com sucesso")
            time.sleep(2)
            LimparTela()
        else:
            print("Renciando urna....")
            time.sleep(3)
            return False
    elif("1" == op and ok [2] == 'True'):
        print("\nVocê ja votou, não pode votar duas vezes :(")
        print("\nVotando ao menu anterior, aguarde!!!")
        time.sleep(4)
        LimparTela()
    elif("2" == op):
        print("Obrigado por sua participação!!! desconectado do servidor....  ")
        time.sleep(5)
        sys.exit()

def Login():
    cont = 0
    list = []
    lista = open('eleitores.txt', 'r+')
    print('''###########################
#       BEM VINDO         #
#           A             #
#  URNA ELETRÔNICA        #
###########################''')
    print("\n \n")
    dados = input("Digite sua matricula para realizar o login: ")
    for k in lista.readlines():
        k = k.split(";")
        if(dados == k[0]):
            nivel = k[3]
            list.append(nivel)
            list.append(cont)
        cont+=1
    if(len(list)==0):
         print("Login Invalido!!!")
         print("Encerrando conexão com servidor...")
         time.sleep(3)
         sys.exit()
    else:
         print("Login realizado com sucesso!!!")
         print("Conectando ao servidor....")
         time.sleep(3)
         LimparTela()
    return list

list = Login()
while(sair):
    if ('a' in list or 'a\n' in list ):
        MenuAdmin(list)
    elif ('b\n' in list or'b' in list ):
       op = MenuUsuario(list)
       if(op == False):
            continue