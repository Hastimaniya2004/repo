#Count vowel,consonant,number and special character
#client file

import socket

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST,PORT))

while True:
    message = input("Enter String (or Exit):");

    if message.lower() == 'exit':
        break

    client_socket.send(message.encode())

    responce = client_socket.recv(1024).decode()

    print(f"Server : {responce}")

client_socket.close()
    
