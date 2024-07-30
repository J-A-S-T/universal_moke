from dotenv import load_dotenv
import socket
import os

load_dotenv()

HOST = os.getenv("MY_MAC_IP")
PORT = int(os.getenv("CONN_PORT"))

with socket.socket( socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(( HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Here your addr is : {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall("I am here and as well")
