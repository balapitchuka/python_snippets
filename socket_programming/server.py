import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) 
while True:
    connection, address = serversocket.accept()
    data = connection.recv(64)
    if len(data) > 0:
            data = data.decode()
            split = data.split("#")
            num1 = split[0]
            operation = split[1]
            num2 = split[2]
    if operation == "+":
                connection.send(str(int(num1) + int(num2)).encode())
    if operation == "-":
                connection.send(str(int(num1) - int(num2)).encode())
    if operation == "*":
                connection.send(str(int(num1) * int(num2)).encode())
    if operation == "/":
                connection.send(str(int(num1) / int(num2)).encode())
