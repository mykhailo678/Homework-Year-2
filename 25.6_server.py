import socket
import os

# Папка для збереження файлів
SAVE_DIR = "uploaded_files"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12346))
server.listen(1)

print("Сервер прийому файлів чекає на клієнта...")

conn, addr = server.accept()
# Спочатку отримуємо ім'я файлу
file_name = conn.recv(1024).decode('utf-8')
file_path = os.path.join(SAVE_DIR, file_name)

with open(file_path, 'wb') as f:
    while True:
        bytes_read = conn.recv(4096)
        if not bytes_read:
            break
        f.write(bytes_read)

print(f"Файл '{file_name}' успішно збережено у каталозі '{SAVE_DIR}'")
conn.close()
server.close()