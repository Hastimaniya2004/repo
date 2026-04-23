#Fibonacci series
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

        print(f"Recevied: {data}")

        a,b = 0,1
        fibo_series = []

        for i in range(int(data)):
            fibo_series.append(str(a))
            c = a+b
            a = b
            b = c
            
        result = "|".join(fibo_series)
        client_socket.send(result.encode())

    client_socket.close()

        
