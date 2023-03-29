import socket
import sys
import time
import json

with socket.socket() as s :

    address = ("localhost",3000) #METTRE L'IP et le canal

    Sub_message = """{"request" : "subscribe", 
                   "port" : 4000,
                   "name" : "Faut être inefficace",
                   "matricules" : ["20145", "21204"]
                   }""".encode()
    try :
        s.connect(address)
    except Exception as error:
        print(error)
        sys.exit
    
    s.send(Sub_message)
    
    response = s.recv(2048).decode()
    print(response)
    jsonrep = json.loads(response) # On transforme le fichier text en format json pour python

    if jsonrep["response"] == "error" : # en cas d'erreur
        print(response["error"])

time.sleep(1) # en attendant
print("ok")
with socket.socket() as s :
    s.settimeout(0.5)
    s.bind(("localhost",5000))
    print(2)
    s.listen()
    print(3)
    while True :
        try :
            client, address = s.accept()
            print(4)
            with client :
                message = json.loads(client.recv(2048).decode()) # On transforme le fichier text en format json pour python
                print(message)
                if message["request"] == "ping" :
                    client.send("""{"response" : "pong"}""".encode())
        except socket.timeout:
            pass