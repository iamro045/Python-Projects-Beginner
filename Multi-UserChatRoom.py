import socket
import threading

clients = []

def broadcast(message, conn):
    for client in clients:
        if client != conn:
            client.send(message)

def handle_client(conn):
    while True:
        try:
            msg = conn.recv(1024)
            broadcast(msg, conn)
        except:
            clients.remove(conn)
            conn.close()
            break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

print("🟢 Chat Server Started")

while True:
    conn, addr = server.accept()
    print("Connected:", addr)
    clients.append(conn)

    thread = threading.Thread(target=handle_client, args=(conn,))
    thread.start()
  
