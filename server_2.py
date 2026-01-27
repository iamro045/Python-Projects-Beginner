import socket

server = socket.socket()
server.bind(("localhost", 9999))
server.listen(1)

print("🟢 Server started")
conn, addr = server.accept()
print("Connected:", addr)

while True:
    msg = conn.recv(1024).decode()
    if msg == "exit":
        break
    print("Client:", msg)
    conn.send("Message received".encode())
