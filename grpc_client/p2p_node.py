from ast import While
import os
import socket
import sys
import threading
import socketserver
from utils import read_in_chunks

HOST, PORT = "localhost", 4001
BUFF_SIZE = 32 * 1024

class P2PNode():
    def SendFile(c, fp):
        size = os.path.getsize(fp)
        c.sendall(size)
        f = open(fp, "rb")
        for chunk in read_in_chunks(f):
            c.sendall(chunk)

    def ReciveFile(c, fp):
        size = c.recv(1024)
        f = open(fp, "wb")
        while size > 0:
            data = c.recv(BUFF_SIZE)
            f.write(data)


class Customer(P2PNode):
    def __init__(self, uuid):
        self.jobUuid = uuid

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def Serve(self, host = HOST, port = PORT):
        self.sock.bind((host, port))
        self.sock.listen(1)
        print(f"Server listening on port {PORT}")
        while True:
            (c, a) = self.sock.accept()
            print (f"[{a}] connected")
            threading.Thread(target=self.HandleConnection, args=(c,)).start()
            

    def HandleConnection(self, c):
        self.SendFile(self.jobUuid+".blend")
        while True:
            fragmentIndex = c.recv(1024)
            if fragmentIndex < 0: break
            self.ReciveFile(fragmentIndex + ".png")

class Worker(P2PNode):
    def __init__(self):
        self.tasks = []
        self.customerIp = ""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def Connect(self, addr):
        '''
        addr format: "0.0.0.0:1234"
        '''
        self.sock.connect(addr)
        



if __name__ == "__main__":
    server = Customer()
    server.Serve()
