import socket
import sys

HOST, PORT = 'localhost', 9999
data = " ".join(sys.argv[1:])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name = input("Input game name: ")

try:
    sock.connect((HOST, PORT))
    sock.sendall(bytes("START,"+ name +",127.0.0.0,9999", "utf-8"))

    received = str(sock.recv(1024), "utf-8")
finally:
    sock.close()

print("Sent:\t{}".format(data))
print("Received:\t{}".format(received))
