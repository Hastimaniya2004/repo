#server file

import socket


def is_vowel():
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or
       ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        return True
    return False

def is_alpha():
    if(ord(ch) >= 65 and ord(ch) <= 90 or ord(ch) >= 96 and ord(ch) <= 122):
        return True
    return False

def is_number():
    if(ord(ch) >= 47 and ord(ch) <= 58):
        return True
    return False




HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST,PORT))

print("Server Running.......");

vowel = 0
consonant = 0
number = 0
special = 0

while True:

    server_socket.listen(5)

    client_socket,addr = server_socket.accept()
    print(f"connect to : {addr}");

    while True:

        data = client_socket.recv(1024).decode()

        if not data:
            break

        print(f"Receive : {data}");

        responce = ''
        for ch in data:
            if(is_alpha()):
                if(is_vowel()):
                    vowel+=1
                else:
                    consonant+=1
            elif(is_number()):
                number+=1
            else:
                special+=1

        responce = f"vowel : {vowel}, consonant : {consonant}, number: {number}, special character :{special}"

        client_socket.send(responce.encode())
    client_socket.close()




