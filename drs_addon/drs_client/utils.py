import os
import subprocess
import socket
import sys

import bpy

def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

class RenderProgressBar():
    sock = None
    client = None
    @classmethod
    def __init__(cls):
        cls.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.sock.bind(("localhost", 4003))
        cls.sock.listen(1)
        #progressScript = os.path.join(bpy.utils.user_resource('SCRIPTS'), 'addons', 'drs_addon', 'scripts', 'progress.py')
        subprocess.Popen(["powershell.exe", sys.executable, "C:\\Users\\lemonhead\\Documents\\AAA diploma blender addon\\drs_addon\\scripts\\progress.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)

        cls.client, _ = cls.sock.accept()
        

    @classmethod
    def Increment(cls):
        cls.client.send(b'hi')

    @classmethod
    def Stop(cls):
        cls.client.send("STOP")
        cls.sock.shutdown(socket.SHUT_RDWR)
        cls.sock.close()

if __name__ == "__main__":
    RenderProgressBar()
    while True:
        if input() == 'stop':
            RenderProgressBar.Stop()
            exit()
        RenderProgressBar.Increment()