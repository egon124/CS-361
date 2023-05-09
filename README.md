# CS-361
Clear instructions for how to REQUEST data from the microservice you implemented. Include an example call.
How to request data: 
HTTP communication begins with a request made by the client. We send this string to the web server, by calling the sendall() method on our socket.
Ex call: 
# create a socket at server side
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_string:
    # bind socket w/ server
    socket_string.bind((host, port))
    socket_string.listen()

    while True:
        conn, addr = socket_string.accept()
        print("Connected by ", addr)
        conn.sendall(b"Create account or sign in :\n\t1. Register \n\t2. Login\n")

Clear instructions for how to RECEIVE data from the microservice you implemented
How to receive data: 
The server should have received the request, and will return a reply with page that requested, by calling recv() method. We convert the byte string by decoding it with decode() method. Once the response is received, the socket will be closed. 
Ex call: 
msg = conn.recv(1024)

        if msg == b'1':
            conn.sendall(b"\nPlease enter your username: ")
            msg = conn.recv(1024)
            with open('user-data.json', 'r') as infile:
                reg_user = json.load(infile)
            username = msg.decode('utf-8')
Please see discussion post for embedded image of UML diagram. 
