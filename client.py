import socket


def client():
    host = ""
    port = 5100

    client_socket = socket.socket()
    client_socket.connect((host, port))
    user = input('Entre votre nom d\'utilisateur : ')
    message = input(f"{user} -> ")
    while message != 'arret':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        if data == 'bye':
            client_socket.close()
            client()
            break
        print('Received from server: ' + data)
        message = input(f"{user}> ")
    client_socket.close()


if __name__ == '__main__':
    client()