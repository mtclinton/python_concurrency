import socket

def client():

    host = ''
    port = 3500

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            sock.connect((host, port))

            m = "testingggg"

            sock.sendall( bytes(m, 'utf-8'))

            data = sock.recv(1024)

    print('Received', data.decode("utf-8"))

    sock.close()


if __name__ == '__main__':
    client()