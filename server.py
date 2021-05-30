import socket
from _thread import start_new_thread
import threading

def server():

    host = "localhost"
    port = 3500

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind((host, port))
    sock.listen(1)
    while True:

        conn, addr = sock.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

    sock.close()


if __name__ == '__main__':
    server()