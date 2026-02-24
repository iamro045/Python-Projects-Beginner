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



start_server()
