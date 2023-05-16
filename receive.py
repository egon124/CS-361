import socket

# create a socket at client side
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect server and port number on local computer
server_address = ('localhost', 10000)
client_sock.connect(server_address)
while True:
	#receive message
	random_num = client_sock.recv(1024).decode()
	pokemon_rec = input()
	client_sock.sendall(pokemon_rec.encode())
	if pokemon_rec == 'end':
		break
print('Socket now closing.')
client_sock.close()