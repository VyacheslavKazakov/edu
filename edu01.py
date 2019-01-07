#!/usr/bin/python3

# Разработать простейший TCP echo сервер.
# Требования
# Запускается на IP адресе 0.0.0.0 и TCP порту 2222
# Получает сообщения длинной не более 1024 байт и отправляет обратно клиенту
# Закрывает соединение при получении сообщения с текстом close﻿

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

def myreceive(sock, msglen):
    msg = ''
    while len(msg) < msglen:
        chunk = sock.recv(msglen-len(msg))
        if chunk == '':
            raise RuntimeError("broken")
            msg = msg + chunk
    return msg


while True:
    conn, addr = s.accept()
    while True:
        # data = conn.recv(1024)
        data = myreceive(s, 1024)
        if not data or data == 'close':
            break
        conn.send(data)
    conn.close()
