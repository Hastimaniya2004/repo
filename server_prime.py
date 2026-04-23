#Prime Number
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
            break;

        print(f"Recevied: {data}")

        prime = False
        for i in range(2,int(data)):
            if(int(data)%i==0):
                prime = True
                break

        if prime:
            result = f"{data} is not prime number"
        else:
            result = f"{data} is prime number"
            
        
        client_socket.send(result.encode())

    client_socket.close()

        
