import logging
from threading import Event
import os
import socket
import threading
from .utils import read_in_chunks

HOST, PORT = "localhost", 4001
FILE_BUFF_SIZE = 32 * 1024
BUFF_SIZE = 1024

class Customer():

    jobDone = Event()
    fragmentN = 0
    hosts = []
    sock = None

    @classmethod
    def CustomerRoutine(cls, addr = (HOST, PORT), workingDir = "", stopEvent = None):
        cls.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        cls.workingDir = workingDir
        cls.jobPath = os.path.join(workingDir, "job.blend")
        cls.sock.bind(addr)
        cls.sock.listen(1)
        print(f"Server listening on port {PORT}")
        logging.info(f"Server listening on port {PORT}")
        threading.Thread(target=cls.Serve, args = (stopEvent,)).start()
        cls.jobDone.wait()
        if stopEvent.is_set():
            return 'STOPPED'
        return 'SUCCESS'

        
            
    @classmethod
    def Serve(cls, stopEvent):
        logging.info("Serving")
        while True:
            (c, a) = cls.sock.accept()
            print (f"[{a}] connected")
            logging.info(f"{a} connected")
            threading.Thread(target=cls.HandleConnection, args=(a, c, stopEvent)).start()

    @classmethod
    def HandleConnection(cls, a, c, stopEvent):
        cls.SendFile(c, cls.jobPath)
        print (f"blend file sent to {a}")
        while True:
            
            if stopEvent.is_set():
                logging.info("Client stopped the routine")
                cls.jobDone.set()
                break
            
            fragmentIndex = int(c.recv(BUFF_SIZE).decode("iso-8859-1"))
            print (f"{a} wants to send fragment {fragmentIndex}")

            if fragmentIndex not in range(100): 
                logging.info(f"{a} host disconnected")
                break

            try:
                fragmentPath = os.path.join(cls.workingDir, str(fragmentIndex) + ".png")
                cls.ReciveFile(c, fragmentPath)
                cls.fragmentN += 1
                print (f"fragment {fragmentIndex} from {a} recived")
                logging.info(f"fragment {fragmentIndex} from {a} recived")
                if cls.fragmentN == 100:
                    Customer.Disconnect()
                    cls.jobDone.set()

            except :
                print(f"[{a}] Error reciving file")
                logging.info(f"[{a}] Error reciving file")
            

    @classmethod
    def SendFile(cls, c, fp):
        size = os.path.getsize(fp)
        c.send(f"{size}".encode("iso-8859-1"))
        logging.debug(f"a file of size {size} will be sent")
        f = open(fp, "rb")
        for chunk in read_in_chunks(f, FILE_BUFF_SIZE):
            c.sendall(chunk)
        f.close()
    
    @classmethod
    def ReciveFile(cls, c, fp):
        size = int(c.recv(BUFF_SIZE).decode("iso-8859-1"))
        print(f"Reciving file of size {size} bytes")
        logging.info(f"Reciving file of size {size} bytes")
        f = open(fp, "wb")
        while size > 0:
            data = c.recv(FILE_BUFF_SIZE)
            f.write(data)
            size -= FILE_BUFF_SIZE
        f.close()

    @classmethod
    def Disconnect(cls):
        cls.sock.shutdown(socket.SHUT_RDWR)
        cls.sock.close()

class Worker():
    
    tasks = []
    customerIp = ""
    sock = None

    @classmethod
    def Connect(cls):
        cls.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.sock.connect((cls.customerIp, 4001))
        logging.info("Connected to customer")

    @classmethod
    def SendFragmentIndex(cls, fi):
        cls.sock.sendall(f"{fi}".encode("iso-8859-1"))
        logging.debug(f"sent fragment index ({fi})")
    
    @classmethod
    def SendFile(cls, fp):
        size = os.path.getsize(fp)
        logging.debug(f"a file of size {size} will be sent")
        cls.sock.send(f"{size}".encode("iso-8859-1"))
        f = open(fp, "rb")
        for chunk in read_in_chunks(f, FILE_BUFF_SIZE):
            cls.sock.sendall(chunk)
        f.close()
        

    @classmethod
    def ReciveFile(cls, fp):
        size = int(cls.sock.recv(BUFF_SIZE).decode("iso-8859-1"))
        print(f"Reciving file of size {size} bytes")
        logging.info(f"Reciving file of size {size} bytes")
        f = open(fp, "wb")
        current_size = 0
        while current_size < size:
            data = cls.sock.recv(1024)
            if not data:
                break
            if len(data) + current_size > size:
                data = data[:size-current_size] 
            f.write(data)
            current_size += len(data)
        f.close()

    @classmethod
    def Disconnect(cls):
        cls.sock.shutdown(socket.SHUT_RDWR)
        cls.sock.close()
