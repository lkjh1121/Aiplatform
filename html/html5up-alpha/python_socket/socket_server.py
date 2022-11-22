import socket

server = socket.socket()
print('[소켓 생성완료]')


server.bind(('192.168.0.104', 999))
server.listen(3)

print('서버 리스닝...')
while True:
    client, address = server.accept()
    name = client.recv(1024).decode()
    print('클라이언트와 연결되었습니다,', address, name)
    client.send(bytes('서버에 연결되었습니다', 'utf-8'))
    client.close()