import socket
import threading
from queue import Queue

# use sockets to connect to certain IP/server at a certain port
# if connection is made its open and vise vera

target = "127.0.0.1" # local host IP
queue = Queue()
open_ports = []

def portscan(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            sock.connect((target, port))
            return True

    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print("Port {} is open! [{}]".format(port, service))
            open_ports.append(port)

port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for t in range(1000):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)