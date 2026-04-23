#Server File

import socket # import socket module for network communication

#define server address and port
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Post number to connect to

#Create a TCP/IP Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to the server using the specified host and port
server_socket.bind((HOST,PORT))

print("Server is running.....")

#kepp the server running continuously
while True:

    #Allow up to 5 queued client connections
    server_socket.listen(5)

    #Accept a connection from a client
    client_socket,addr = server_socket.accept()
    print(f"Connected by {addr}")   #Display client address

    #continuously receive data from the connected client
    while True:
        #receive data (max 1024 bytes) and decode it into a string
        data = client_socket.recv(1024).decode()

        #if no data is received, the client has disconnected
        if not data:
            break

        print(f"Received: {data}")

        #convert received message to uppercase
        response = data.upper()

        #send the modified responce back to the client
        client_socket.send(response.encode())

    #close the client connection after communication ends
    client_socket.close()
