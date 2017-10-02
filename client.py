from socket import *

CLIENT_OPTIONS = ["user_login", "os", "network", "system_release", "system_version", "hardware"]
BUFFER_SIZE = 64000


def menu():
    info = """
    Options:
        User Login
        OS
        Network
        System Release
        System Version
        Hardware
    """
    print(info)


def client_main():
    menu()
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((gethostname(), 9000))

    while True:
        option = input("Option: ").lower()

        # normalize user input
        user_option = option.replace(" ", "_")

        if user_option in CLIENT_OPTIONS:
            response = get_answer(client, user_option)
            print(response)
        else:
            print("Leave? ")
            answer = input('y/n: ').lower()
            if answer == 'y':
                break
            else:
                continue


def get_answer(client_socket, message):
    client_socket.send(message.encode('utf8'))
    response = client_socket.recv(BUFFER_SIZE).decode('utf8')
    return response

client_main()
