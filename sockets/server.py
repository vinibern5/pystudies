#servidor

# server.py
from socket import *
from time import asctime,sleep
import os,sys
# create a socket object
server = socket(AF_INET,SOCK_STREAM)
# Nome da nossa máquina
host = gethostname()
port = 9999
# Ativa o socket
server.bind((host, port))
# O servidor está aceitando novas conexões 
server.listen()

recebe = lambda sckt: sckt.recv(1024).decode('utf8') #Func p/ receber msgs
envia = lambda sckt, msg: sckt.send(msg.encode('utf8')) #Func p/ enviar msgs

print("Em espera...")
# Aceita uma conexão (fica aguardando por uma conexão)
client,addr = server.accept() #cliente = socket p/ cliente / addr = endereço
print("Conexão recebida de: %s" % str(addr))
envia(client,'Conexão ativa!')
tempo = asctime()
login = os.getlogin()
cores = str(os.cpu_count())
versao = ('Windows ' + str(sys.getwindowsversion().major)
+ ' Build ' + str(sys.getwindowsversion().build))
dirct = os.getcwd()
pid = str(os.getpid())

while True:
    ordem = recebe(client)
    if ordem == '1':
        envia(client, tempo)
    elif ordem == '2':
        envia(client, login)
    elif ordem == '3':
        envia(client, cores)
    elif ordem == '4':
        envia(client, versao)
    elif ordem == '5':
        envia(client, dirct)
    elif ordem == '6':
        envia(client, pid)
    elif ordem == '7':
        os.system('calc.exe')
        envia(client,'Aberto com sucesso!')
    elif ordem == '8':
        os.system('py')
        envia(client,'Aberto com sucesso!')
    elif ordem == '0':
        client.close()
        server.close()
        print('Saindo da aplicação...')
        sleep(2)
        break
        
        
    
