# About
This microservice utilizes socket programming to generate a random number. 
# How to request data: 
Create a TCP/IP socket (i.e.: socket.socket(socket.AF_INET, socket.SOCK_STREAM)) and subsequently connect the socket to the address of the server using connect() system call, attaching the the socket directly to the remote address. In this case, the address is 'localhost' (current server), and the port number is '10000'. The socket is now connected to the port where the server is listening. Once the connection is established, data may sent through the socket with sendall() & received with recv(), which are methods that may be used server-side as well. 
# How to receive data: 
Create a TCP/IP socket(i.e.: socket.socket(socket.AF_INET, socket.SOCK_STREAM)) and subsequently bind the socket to an address using the bind() system call, which will associate the socket with the server address (localhost, 10000). Listen for connections with the listen() system call, accept a connection with the accept() system call, data may now be sent and/or received via the socket. The accept() call will return an open connection between server and client. Read the data from the connection with recv() call and send data through socket with sendall() call. 

![UML](https://github.com/egon124/CS-361/assets/108035300/1d967f98-77ad-46fe-b3e4-e724b7df7c73)
