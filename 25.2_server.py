import socket


def check_syntax(expression):
    try:
        compile(expression, '<string>', 'eval')
        return "Синтаксис коректний"
    except SyntaxError as e:
        return f"Помилка синтаксису: {e.msg}"
    except Exception:
        return "Некоректний вираз"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)

print("Сервер перевірки виразів запущено...")

while True:
    conn, addr = server.accept()
    data = conn.recv(1024).decode('utf-8')
    if not data:
        break

    print(f"Отримано вираз: {data}")
    result = check_syntax(data)
    conn.send(result.encode('utf-8'))
    conn.close()