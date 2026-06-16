import socket

# use sockets to connect to certain IP/server at a certain port
# if connection is made its open and vise vera

target = "127.0.0.1" # local host IP

def portscan(port):
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True

    except: 
        return False

for port in range (1, 1024):
    result = portscan(port)
    if result:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"
        print("Port {} is open! [{}]".format(port, service))
    else: 
        print("Port {} is closed!".format(port))