
# client.py
from socket import *
from time import sleep

recebe = lambda sckt: sckt.recv(1024).decode('utf8') #Func p/ receber msgs
envia = lambda sckt, msg: sckt.send(msg.encode('utf8')) #Func p/ enviar msgs

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
9 - 
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
    elif op == '0':
        envia(s,'0')
        print('Saindo da aplicação...')
        s.close()
        sleep(2)
        return True
    


 # create a socket object
s = socket(AF_INET, SOCK_STREAM)
 # get local machine name
host = gethostname()
port = 9999
 # connection to hostname on the port.
s.connect((host, port))
status = recebe(s)
print(status)


#s.send('Comunicação estabelecida!'.encode('utf8'))

while True:
    if menu() == True:
        break
    print(recebe(s))


#s.close()
