import socket

server = socket.socket()
server.bind(("localhost", 9000))
server.listen(1)

conn, _ = server.accept()

with open("sample.txt", "rb") as f:
    conn.sendall(f.read())

conn.close()
