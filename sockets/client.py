
# client.py
from socket import *
from time import sleep

def recebe(sckt):
    return sckt.recv(1024).decode('utf8') #Func p/ receber msgs
def envia(sckt, msg):
    sckt.send(msg.encode('utf8')) #Func p/ enviar msgs

def menu(): 
    opcs =''' 
1 - Data
2 - Nome do computador
3 - Quantidade de núcleos
4 - Versão do Windows
5 - Diretório do servidor
6 - ID do processo do servidor
7 - Abrir a calculadora
8 - Abrir um terminal python pelo cmd (talvez não funcione por configs de PATH)
9 - Tempo de usuário no processo servidor
10 - Tempo do sistema no processo servidor
0 - Sair


'''
    print(opcs)
    op = input("Opção: ")
    if op == '1':
        envia(s,'1')
    elif op == '2':
        envia(s,'2')
    elif op == '3':
        envia(s,'3')
    elif op == '4':
        envia(s,'4')
    elif op == '5':
        envia(s,'5')
    elif op == '6':
        envia(s,'6')
    elif op == '7':
        envia(s,'7')
    elif op == '8':
        envia(s,'8')
    elif op == '9':
        envia(s,'9')
    elif op == '10':
        envia(s,'10')
    elif op == '0':
        envia(s,'0')
        print('Saindo da aplicação...')
        s.close()
        sleep(2)
        return True 
    else:
        print('Opção invalida!')
        return menu()


#Instancia um objeto do tipo socket
s = socket(AF_INET, SOCK_STREAM)

host = gethostname()
port = 9999

s.connect((host, port)) #Se conecta com o nosso servidor
status = recebe(s)
print(status)



while True:
    if menu() == True:
        break
    print(recebe(s))



