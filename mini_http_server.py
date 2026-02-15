import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8080))
server.listen(5)

print("🌐 Server running on http://localhost:8080")

while True:
    client_socket, addr = server.accept()
    request = client_socket.recv(1024).decode()
    print("📩 Request:\n", request)

    response = """HTTP/1.1 200 OK
Content-Type: text/html

<h1>Hello Rohit 🚀</h1>
<p>This is your own HTTP server!</p>
"""
    client_socket.send(response.encode())
    client_socket.close()
