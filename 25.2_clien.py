import socket

expression = input("Введіть арифметичний вираз: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))
client.send(expression.encode('utf-8'))

response = client.recv(1024).decode('utf-8')
print(f"Відповідь сервера: {response}")
client.close()