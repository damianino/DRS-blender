import threading
import queue

q = queue.Queue()

def executor():
    while True:
        item = q.get()
        if item == "stop": return
        print(item)

def cli():
    while True:
        item = input(">>>")
        q.put(item)
        if item == "stop": return

threading.Thread(target=cli).start()
threading.Thread(target=executor).start()
