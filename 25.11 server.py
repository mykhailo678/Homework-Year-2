import socket


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5555))
    server_socket.listen(2)

    conn1, addr1 = server_socket.accept()
    conn1.send("Connected as Client 1. Wait for Client 2...".encode())

    conn2, addr2 = server_socket.accept()
    conn2.send("Connected as Client 2. Start!".encode())

    try:
        while True:
            msg1 = conn1.recv(1024)
            if not msg1: break
            conn2.send(msg1)

            msg2 = conn2.recv(1024)
            if not msg2: break
            conn1.send(msg2)
    except:
        pass
    finally:
        conn1.close()
        conn2.close()
        server_socket.close()


if __name__ == "__main__":
    start_server()