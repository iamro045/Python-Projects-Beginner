import socket

routes = {}

def route(path):
    def decorator(func):
        routes[path] = func
        return func
    return decorator

@route("/")
def home():
    return "HTTP/1.1 200 OK\n\nWelcome to Mini Framework 🚀"

@route("/about")
def about():
    return "HTTP/1.1 200 OK\n\nAbout Page"

def start_server():
    server = socket.socket()
    server.bind(("localhost", 8081))
    server.listen(5)
    print("Server running at http://localhost:8081")

    while True:
        client, _ = server.accept()
        request = client.recv(1024).decode()
        path = request.split(" ")[1]

        response = routes.get(path, lambda: "HTTP/1.1 404\n\nNot Found")()
        client.send(response.encode())
        client.close()


start_server()
