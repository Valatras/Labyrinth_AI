import socket
import sys
import time
import json

server_address = ("localhost",3000) #METTRE L'IP et le canal

with socket.socket() as s :

    
    Sub_message = """{"request" : "subscribe", 
                   "port" : 5000,
                   "name" : "Faut être efficace",
                   "matricules" : ["20144", "21203"]
                   }""".encode()
    try :
        s.connect(server_address)
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
print(1)
with socket.socket() as s :
    s.settimeout(0.5)
    s.bind(("",5000))
    print(2)
    s.listen()
    print(3)
    while True :
        try :
            client, address = s.accept()
            print(4)
            with client :
                message = json.loads(client.recv(16600).decode()) # On transforme le fichier text en format json pour python
                for keys in message.keys():
                    if keys == "state" or keys == "errors":
                        party_state = message["state"] #on récupère l'état de la partie
                        
                    else: 
                        print(keys, " : ", message[keys])
                    

                if message["request"] == "ping" :
                    client.send("""{"response" : "pong"}""".encode())

                elif message["request"] == "play":
                    move_setup = {
                        "tile": party_state["tile"],
                        "gate": "A",
                        "new_position": 0
                    }
                            
                    moving = {
                            "response": "move",
                            "move": move_setup,
                            "message": "Fun message"
                            }
                    
                    client.send(json.dumps(moving).encode())
                        
                    
            print("e")
        except socket.timeout:
            print("trop tard")
                
    
    

