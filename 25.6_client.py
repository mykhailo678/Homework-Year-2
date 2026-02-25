import socket
import os

file_path = input("Введіть шлях до файлу, який треба відправити: ")

if os.path.exists(file_path):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12346))

    # Відправляємо назву файлу (тільки ім'я, без шляху)
    file_name = os.path.basename(file_path)
    client.send(file_name.encode('utf-8'))

    # Невелика пауза, щоб сервер встиг обробити назву
    import time

    time.sleep(0.1)

    # Відправляємо вміст файлу
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            client.sendall(data)

    print("Файл відправлено.")
    client.close()
else:
    print("Файл не знайдено.")