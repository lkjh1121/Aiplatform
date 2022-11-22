import socket
client = socket.socket()
c_name = socket.gethostname()
client.connect(('192.168.0.104', 999))
name = input("이름을 입력하세요")
client.send(bytes(name, 'utf-8'))
print(client.recv(1024).decode())