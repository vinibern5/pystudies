from socket import *
import os

addr = (gethostname(), 9000)
server = socket(AF_INET, SOCK_STREAM)
server.bind(addr)


def server_main():
    server.listen(1)

    client, client_address = server.accept()
    uname = os.uname()
    while True:
        client_option = client.recv(1024).decode('utf8')
        if client_option == 'os':
            response = os.name()
            client.send(response.encode('utf8'))
        elif client_option == 'user_login':
            response = os.getlogin()
            client.send(response.encode('utf8'))
        elif client_option == 'network':
            response = uname[1]
            client.send(response[0].encode('utf8'))
        elif client_option == 'system_release':
            response = uname[2]
            client.send(response.encode('utf8'))
        elif client_option == 'system_version':
            response = uname[3]
            client.send(response.encode('utf8'))
        elif client_option == 'hardware':
            response = uname[4]
            client.send(response.encode('utf8'))

while True:
    server_main()
