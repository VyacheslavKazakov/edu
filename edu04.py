#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Разработать простейший TCP echo сервер.
# Требования
# Запускается на IP адресе 0.0.0.0 и TCP порту 2222
# Получает сообщения длинной не более 1024 байт и отправляет обратно клиенту
# Закрывает соединение при получении сообщения с текстом close﻿
# + Измените ваш echo сервер так, что бы он работать одновременно с 10 клиентами.

# Задача на threading.

import socket
import threading
import logging

class MyThread(threading.Thread):

    def __init__(self, conn, logger):
        threading.Thread.__init__(self)
        self.conn = conn
        self.logger = logger


    def run(self):
        """
        Run the thread
        """
        logger.debug('Calling server')
        server(self.conn, self.logger)


def get_logger():
    logger = logging.getLogger("threading_example")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("threading_class.log")
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
logger = get_logger()

def server(conn, logger):
    while True:
        data = conn.recv(1024)
        logger.debug('server executing')
        logger.debug('server process ended with: {}'.format(data))
        if not data or data == b'close':
            break
        conn.send(data)
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connection", addr)
    t = MyThread(conn, logger)
    t.start()
