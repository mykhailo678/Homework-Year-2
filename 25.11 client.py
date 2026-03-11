import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5555))

    print(client_socket.recv(1024).decode())

    try:
        while True:
            message = input("You: ")
            client_socket.send(message.encode())
            if message.lower() == 'exit': break

            data = client_socket.recv(1024).decode()
            if not data: break
            print(f"Partner: {data}")
    except:
        pass
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()