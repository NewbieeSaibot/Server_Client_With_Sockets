#A simple server made by Tobias Rossi Müller because quarantine is very boring. Based on tech with tim channel
import threading
import socket

port = 5000 # i dont know why but i like this number
header = 64
format = "utf-8"
dsiconnect_message = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname()) #this will return my local ip
address = (SERVER, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(header).decode(format)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(format)
            if msg == dsiconnect_message:
                connected = False #break the loop
            print(f"[{addr}] sent {msg}")
            conn.send("Msg received".encode(format))

def start():
    server.listen()
    print("Listening on ", {server})
    while(True):
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f" We have {threading.activeCount() - 1} active connections!!") # one thread is the start function running forever

print("starting the server")
start()