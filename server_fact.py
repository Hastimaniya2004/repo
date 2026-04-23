#Factorial
#Server File

import socket

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind((HOST,PORT))

print("Server Running.....")

while True:
    server_socket.listen(5)

    client_socket,addr = server_socket.accept()

    print(f"Connected by {addr}")

    while True:
        data = client_socket.recv(1024).decode()

        if not data:
            break

        print(f"Received: {data}")

        response = ''
        fact = 1
        for i in range(1,int(data)+1):
            fact*=i

        response = f"{fact}"

        client_socket.send(response.encode())

    client_socket.close()
            




        
