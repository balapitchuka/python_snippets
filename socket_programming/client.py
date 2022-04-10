import socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))

value = input("send operation like this 2#+#3")
clientsocket.send(value.encode())
msg = clientsocket.recv(1024)
print(msg.decode())