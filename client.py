import socket
import os


HOST = os.getenv("MY_WIN_IP")
PORT = os.getenv("CONN_PORT")

with socket.socket( socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(( HOST, PORT))
    s.sendall("Hello brother connecting with you")
    data = s.recv(1024)
print(f"Recived data : {data}")