import socket
import sys
import time

with socket.socket() as s :

    address = (,8888) #METTRE L'IP et le canal

    Sub_message = {"request" : "subscribe", 
                   "port" : 8888,
                   "name" : "Faut être efficace",
                   "matricules" : ["20144", "21203"]
                   }.encode()
    try :
        s.connect(address)
    except Exception as error:
        print(error)
        sys.exit
    
    s.send(Sub_message)
    
    response = s.recv(2048).decode()

    if response[0] == "error" : # en cas d'erreur
        print(response[1])

    time.sleep(1) # en attendant

    response = s.recv(2048).decode()

    if response[0] == "ping" :
        s.send(("pong").encode())
    

