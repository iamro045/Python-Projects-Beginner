import socket

target = input("Enter target host: ")

print("Scanning ports...")

for port in range(20, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print("Open port:", port)

    sock.close()
