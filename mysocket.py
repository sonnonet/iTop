# -*- coding: utf8 -*-


from socket import *
from select import select
import sys



HOST = '125.7.128.41'
PORT = 56789
BUFSIZE = 1024
ADDR = (HOST, PORT)


clientSocket = socket(AF_INET, SOCK_STREAM)


try:
    clientSocket.connect(ADDR)
except Exception as e:
    print('Cant(%s:%s)Connection' % ADDR)
    sys.exit()
print('connection server (%s:%s).' % ADDR)


def prompt():
    sys.stdout.write('<me> ')
    sys.stdout.flush()


while True:
    try:
        connection_list = [sys.stdin, clientSocket]

        read_socket, write_socket, error_socket = select(connection_list, [], [], 10)

        for sock in read_socket:
            if sock == clientSocket:
                data = sock.recv(BUFSIZE)
                if not data:
                    clientSocket.close()
                    sys.exit()
                else:
                    print('%s' % data) 
                    prompt()
            else:
                message = sys.stdin.readline()
                clientSocket.send(message)
                prompt()
    except KeyboardInterrupt:
        clientSocket.close()
        sys.exit()
