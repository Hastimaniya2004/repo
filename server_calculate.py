#calculation
#Server File

import socket

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind((HOST,PORT))

print("Server Running....")

while True:

    server_socket.listen(5)

    client_socket,addr = server_socket.accept()

    print(f"connected by {addr}")

    while True:
        data = client_socket.recv(1024).decode()

        if not data:
            break

        print(f"Received : {data}")

        try:
            operand1,operator,operand2 = data.split()

            operand1,operand2 = float(operand1),float(operand2)

            if operator == '+':
                result = operand1 + operand2
            elif operator == '-':
                result = operand1 - operand2
            elif operator == '*':
                result = operand1 * operand2
            elif operator == '/':
                if operand2 == 0:
                    result = "error: Division by zero"
                else:
                    result = operand1 / operand2
            else:
                resulr = "error: Invalid operator"

        except Exception as e:
            print(e)

        response = f"{result}"

        client_socket.send(response.encode())

    client_socket.close()
                

