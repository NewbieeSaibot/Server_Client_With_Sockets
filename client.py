import socket

port = 5000 # i dont know why but i like this number
header = 64
format = "utf-8"
dsiconnect_message = "!DISCONNECT"
server = "192.168.2.9"
address = (server, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

def send(msg):
    message = msg.encode(format)
    msg_length = len(message)
    send_length = str(msg_length).encode(format)
    send_length += b' '  * (header - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(format))
    
def disconnect():
    send(dsiconnect_message)

send("Hello World!")
disconnect()