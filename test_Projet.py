import socket
import json
from Search_algorithm import showBoard, PriorityQueue, BestFS, find_target, cord, successors, heuristic

def test_showBoard(capsys):
    board = [
        {"N": True, "E": False, "S": True, "W": True, "item": None},
        {"N": False, "E": True, "S": False, "W": False, "item": 1},
        {"N": True, "E": False, "S": True, "W": True, "item": 2},
        {"N": True, "E": True, "S": False, "W": True, "item": 3},
    ]
    showBoard(board)
    captured = capsys.readouterr()
    assert captured.out.strip() == """
# # #|  
# A #|  
# # #|  
- - -|  
 |#   
 |B   
 |#   
- - -|  
# # #|  
C D #|  
# # #|  
- - -|  
# # #|  
# # #|  
# E F|
- - -|  
""".strip()


def test_PriorityQueue():
    queue = PriorityQueue()
    queue.enqueue("A", 3)
    queue.enqueue("B", 1)
    queue.enqueue("C", 2)

    assert queue.dequeue() == "B"
    assert queue.dequeue() == "C"
    assert queue.dequeue() == "A"
    assert queue.isEmpty()


def test_BestFS():
    def successors(node, free_tile, state):
        return [(free_tile, "A", 2), (free_tile, "B", 3)]

    def heuristic(new_node, target):
        return abs(new_node - target)

    state = {
        "board": [
            {"N": True, "E": False, "S": True, "W": True, "item": None},
            {"N": False, "E": True, "S": False, "W": False, "item": 1},
            {"N": True, "E": False, "S": True, "W": True, "item": 2},
            {"N": True, "E": True, "S": False, "W": True, "item": 3},
        ],
        "target": 1,
        "current": 0,
    }

    move = BestFS((None, None, 0), successors, heuristic, state, 0)

    assert move == [0, "A", 2]


def test_find_target():
    state = {
        "board": [
            {"N": True, "E": False, "S": True, "W": True, "item": None},
            {"N": False, "E": True, "S": False, "W": False, "item": 1},
            {"N": True, "E": False, "S": True, "W": True, "item": 2},
            {"N": True, "E": True, "S": False, "W": True, "item": 3},
        ],
        "target": 1,
    }

    assert find_target(state) == 1

    state["board"][1]["item"] = None
    assert find_target(state) == False

def test_successors():
    current = 13
    free_tile = {'N': True, 'E': False, 'S': False, 'W': True}
    board = {
        0: {'N': True, 'E': False, 'S': True, 'W': False},
        1: {'N': False, 'E': False, 'S': True, 'W': True},
        2: {'N': True, 'E': False, 'S': False, 'W': True},
        3: {'N': False, 'E': True, 'S': True, 'W': False},
        4: {'N': False, 'E': True, 'S': False, 'W': True},
        5: {'N': True, 'E': True, 'S': True, 'W': True},
        6: {'N': True, 'E': True, 'S': True, 'W': True},
        7: {'N': True, 'E': False, 'S': False, 'W': False},
        8: {'N': False, 'E': True, 'S': False, 'W': False},
        9: {'N': False, 'E': False, 'S': True, 'W': False},
        10: {'N': False, 'E': False, 'S': False, 'W': True},
        11: {'N': True, 'E': False, 'S': False, 'W': False},
        12: {'N': False, 'E': True, 'S': False, 'W': False},
        13: {'N': False, 'E': True, 'S': False, 'W': False},
        14: {'N': False, 'E': True, 'S': False, 'W': False},
        15: {'N': False, 'E': True, 'S': False, 'W': False},
        16: {'N': False, 'E': True, 'S': False, 'W': False},
        17: {'N': False, 'E': True, 'S': False, 'W': False},
        18: {'N': False, 'E': True, 'S': False, 'W': False},
        19: {'N': False, 'E': True, 'S': False, 'W': False},
        20: {'N': False, 'E': True, 'S': False, 'W': False},
        21: {'N': False, 'E': True, 'S': False, 'W': False},
        22: {'N': False, 'E': True, 'S': False, 'W': False},
        23: {'N': False, 'E': True, 'S': False, 'W': False},
        24: {'N': False, 'E': True, 'S': False, 'W': False},
        25: {'N': False, 'E': True, 'S': False, 'W': False},
        26: {'N': False, 'E': True, 'S': False, 'W': False},
        27: {'N': False, 'E': True, 'S': False, 'W': False},
        28: {'N': False, 'E': True, 'S': False, 'W': False},
        29: {'N': False, 'E': True, 'S': False, 'W': False},
        30: {'N': False, 'E': True, 'S': False, 'W': False},
        31: {'N': False, 'E': True, 'S': False, 'W': False},
        32: {'N': False, 'E': True, 'S': False, 'W': False},
        33: {'N': False, 'E': True, 'S': False, 'W': False},
        34: {'N': False, 'E': True, 'S': False, 'W': False},
        35: {'N': False, 'E': True, 'S': False, 'W': False},
        36: {'N': False, 'E': True, 'S': False, 'W': False},
        37: {'N': False, 'E': True, 'S': False, 'W': False},
        38: {'N': False, 'E': True, 'S': False, 'W': False},
        39: {'N': False, 'E': True, 'S': False, 'W': False},
        40: {'N': False, 'E': True, 'S': False, 'W': False},
        41: {'N': False, 'E': True, 'S': False, 'W': False},
        42: {'N': False, 'E': True, 'S': False, 'W': False},
        43: {'N': False, 'E': True, 'S': False, 'W': False},
        44: {'N': False, 'E': True, 'S': False, 'W': False},
        45: {'N': False, 'E': True, 'S': False, 'W': False},
        46: {'N': False, 'E': True, 'S': False, 'W': False},
        47: {'N': False, 'E': True, 'S': False, 'W': False}
    }

    state = {
        'current': current,
        'board': board
    }

    node = 16

    # Expected successors
    expected_successors = [
        ({'N': True, 'E': False, 'S': False, 'W': True}, 'A', 7),
        ({'N': False, 'E': True, 'S': False, 'W': True}, 'A', 14),
        ({'N': True, 'E': True, 'S': True, 'W': True}, 'A', 17),
        ({'N': False, 'E': False, 'S': True, 'W': True}, 'A', 23),
        ({'N': True, 'E': False, 'S': False, 'W': True}, 'B', 21),
        ({'N': False, 'E': True, 'S': False, 'W': True}, 'B', 28),
        ({'N': True, 'E': True, 'S': True, 'W': True}, 'B', 31),
        ({'N': False, 'E': False, 'S': True, 'W': True}, 'B', 37),
        ({'N': True, 'E': False, 'S': False, 'W': True}, 'C', 35),
                ({'N': False, 'E': True, 'S': False, 'W': True}, 'C', 42),
        ({'N': True, 'E': True, 'S': True, 'W': True}, 'C', 45),
        ({'N': False, 'E': False, 'S': True, 'W': True}, 'C', 51),
        ({'N': True, 'E': False, 'S': False, 'W': True}, 'D', 5),
        ({'N': False, 'E': True, 'S': False, 'W': True}, 'D', 12),
        ({'N': True, 'E': True, 'S': True, 'W': True}, 'D', 15),
        ({'N': False, 'E': False, 'S': True, 'W': True}, 'D', 21),
        ({'N': True, 'E': False, 'S': False, 'W': True}, 'E', 19),
        ({'N': False, 'E': True, 'S': False, 'W': True}, 'E', 26),
        ({'N': True, 'E': True, 'S': True, 'W': True}, 'E', 29),
        ({'N': False, 'E': False, 'S': True, 'W': True}, 'E', 35),
        ({'N': True, 'E': False, 'S': False, 'W': True}, 'F', 33),
        ({'N': False, 'E': True, 'S': False, 'W': True}, 'F', 40),
        ({'N': True, 'E': True, 'S': True, 'W': True}, 'F', 43),
        ({'N': False, 'E': False, 'S': True, 'W': True}, 'F', 49),
        ({'N': True, 'E': False, 'S': False, 'W': True}, 'G', 47),
        ({'N': False, 'E': True, 'S': False, 'W': True}, 'G', 4),
        ({'N': True, 'E': True, 'S': True, 'W': True}, 'G', 7),
        ({'N': False, 'E': False, 'S': True, 'W': True}, 'G', 13),
        ({'N': True, 'E': False, 'S': False, 'W': True}, 'H', 45),
        ({'N': False, 'E': True, 'S': False, 'W': True}, 'H', 2),
        ({'N': True, 'E': True, 'S': True, 'W': True}, 'H', 5),
        ({'N': False, 'E': False, 'S': True, 'W': True}, 'H', 11),
        ({'N': True, 'E': False, 'S': False, 'W': True}, 'I', 43),
        ({'N': False, 'E': True, 'S': False, 'W': True}, 'I', 0),
        ({'N': True, 'E': True, 'S': True, 'W': True}, 'I', 3),
        ({'N': False, 'E': False, 'S': True,'W': True}, 'I', 9),
        ({'N': True, 'E': False, 'S': False, 'W': True}, 'J', 35),
        ({'N': False, 'E': True, 'S': False, 'W': True}, 'J', 42),
        ({'N': True, 'E': True, 'S': True, 'W': True}, 'J', 45),
        ({'N': False, 'E': False, 'S': True, 'W': True}, 'J', 51),
        ({'N': True, 'E': False, 'S': False, 'W': True}, 'K', 21),
        ({'N': False, 'E': True, 'S': False, 'W': True}, 'K', 28),
        ({'N': True, 'E': True, 'S': True, 'W': True}, 'K', 31),
        ({'N': False, 'E': False, 'S': True, 'W': True}, 'K', 37),
        ({'N': True, 'E': False, 'S': False, 'W': True}, 'L', 7),
        ({'N': False, 'E': True, 'S': False, 'W': True}, 'L', 14),
        ({'N': True, 'E': True, 'S': True, 'W': True}, 'L', 17),
        ({'N': False, 'E': False, 'S': True, 'W': True}, 'L', 23)
    ]

    # Obtain the actual successors
    actual_successors = successors(node, free_tile, state)

    # Sort the successors for comparison
    actual_successors = sorted(actual_successors, key=lambda x: (x[1], x[2]))

    # Compare the expected and actual successors
    assert actual_successors == expected_successors, "Test case 1 failed"




def test_cord():
    assert cord(0) == [0, 0]
    assert cord(6) == [6, 0]
    assert cord(7) == [0, 1]
    assert cord(13) == [6, 1]
    assert cord(14) == [0, 2]
    assert cord(20) == [6, 2]
    assert cord(27) == [6, 3]


def test_heuristic():
    assert heuristic(0, 14) == 2.0
    assert heuristic(13, 13) == 0.0

def test_subscribe_to_server():
     with socket.socket() as s:
        server_address = ("localhost", 3000)  # Update with the correct server address
        try:
            s.connect(server_address)
        except Exception as error:
            assert False, f"Failed to connect to the server: {error}"
        else:
            assert True, "Server connection successful"

def test_ping_request():
    with socket.socket() as s:
        s.settimeout(0.5)
        s.bind(("", 5000))
        s.listen()

        # Prepare a test message
        test_message = {
            "request": "ping",
            "data": "Test data"
        }
        encoded_message = json.dumps(test_message).encode()

        # Connect and send the test message
        with socket.socket() as client_socket:
            client_socket.connect(("localhost", 5000))
            client_socket.send(encoded_message)

        try:
            client, address = s.accept()
            with client:
                message = json.loads(client.recv(16600).decode())

                # Verify the received message
                assert message["request"] == "ping"
                assert message["data"] == "Test data"
                
                # Prepare and send a response message
                response_message = {
                    "response": "pong"
                }
                encoded_response = json.dumps(response_message).encode()
                client.send(encoded_response)

        except socket.timeout:
            assert False, "Test timed out"