from dotenv import load_dotenv
import socket
import os

load_dotenv()

HOST = "0.0.0.0"
PORT = int(os.getenv("CONN_PORT"))

with socket.socket( socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(( HOST, PORT))
    s.sendall("Hello brother connecting with you")
    data = s.recv(1024)
print(f"Recived data : {data}")