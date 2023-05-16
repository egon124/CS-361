import socket
import random

# create a socket at server side
socket_string = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind socket to port
server_address = ('localhost', 10000)
socket_string.bind(server_address)

#establish how many clients the server can listen to
socket_string.listen(1)

while True:
    conn, addr = socket_string.accept()
    print("Connected by ", addr)
    try:
        random_num = random.randit(1, 1008)
        print ('Your randomly generator number is: ', random_num)

        conn.sendall(str(random_num).encode())

        while True:
            pokemon_rec = conn.recv(1024)
            pokemon_rec = pokemon_rec.decode()
            print ('Your randomly generated pokemon is', pokemon_rec)
    finally:
        conn.close()



