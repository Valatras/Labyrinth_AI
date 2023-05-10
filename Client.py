import socket
import sys
import time
import json
from Search_algorithm import *

def subscribe_to_server():
    server_address = ("localhost", 3000)  # METTRE L'IP et le canal
    with socket.socket() as s:
        Sub_message = {
            "request": "subscribe",
            "port": 5000,
            "name": "Faut Ãªtre efficace",
            "matricules": ["20144", "21203"]
        }
        try:
            s.connect(server_address)
        except Exception as error:
            print(error)
            sys.exit()
        
        s.send(json.dumps(Sub_message).encode())
        response = s.recv(2048).decode()
        print(response)
        jsonrep = json.loads(response)
        
        if jsonrep["response"] == "error":
            print(response["error"])

def receive_message_from_client():
    with socket.socket() as s:
        s.settimeout(0.5)
        s.bind(("", 5000))
        s.listen()
        
        while True:
            try:
                client, address = s.accept()
                print(4)
                with client:
                    message = json.loads(client.recv(16600).decode())
                    print([message.keys()])
                    
                    for keys in message.keys():
                        if keys == "state" or keys == "errors":
                            party_state = message["state"]
                        else:
                            print(keys, " : ", message[keys])
                    
                    if message["request"] == "ping":
                        client.send("""{"response" : "pong"}""".encode())
                    
                    elif message["request"] == "play":
                        party_state = message['state']
                        print(showBoard(party_state['board']))
                        move_finder = BestFS((None, None, party_state['current']), successors, heuristic, party_state, party_state['tile'])
                        print(move_finder)
                        move_setup = {
                            "tile": move_finder[0],
                            "gate": move_finder[1],
                            "new_position": move_finder[2]
                        }
                        
                        moving = {
                            "response": "move",
                            "move": move_setup,
                            "message": "Fun message"
                        }
                        
                        client.send(json.dumps(moving).encode())
            except socket.timeout:
                pass

def main():
    subscribe_to_server()
    time.sleep(1)
    print(1)
    receive_message_from_client()

if __name__ == "__main__":
    main()