#!/usr/bin/python3

# Разработать простейший TCP echo сервер.
# Требования
# Запускается на IP адресе 0.0.0.0 и TCP порту 2222
# Получает сообщения длинной не более 1024 байт и отправляет обратно клиенту
# Закрывает соединение при получении сообщения с текстом close﻿
# + Измените ваш echo сервер так, что бы он работать одновременно с 10 клиентами.

import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

def server(conn,):
    while True:
        data = conn.recv(1024)
        if not data or data == b'close':
            break
        conn.send(data)
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connection", addr)
    t = threading.Thread(target=server, args=(conn, ))
    t.start()
