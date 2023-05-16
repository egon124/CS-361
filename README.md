# CS-361
Clear instructions for how to REQUEST data from the microservice you implemented. Include an example call.
# How to request data: 
HTTP communication begins with a request made by the client. We send this string to the web server, by calling the sendall() method on our socket.
Ex call: 
conn.sendall(str(random_num).encode())

Clear instructions for how to RECEIVE data from the microservice you implemented
# How to receive data: 
The server should have received the request, and will return a reply with page that requested, by calling recv() method. We convert the byte string by decoding it with decode() method. Once the response is received, the socket will be closed. 
Ex call: 
        while True:
            pokemon_rec = conn.recv(1024)
            pokemon_rec = pokemon_rec.decode()
            print ('Your randomly generated pokemon is', pokemon_rec)
    finally:
        conn.close()
Please see discussion post for embedded image of UML diagram. 
