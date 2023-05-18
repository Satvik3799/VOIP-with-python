import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostbyname(socket.gethostname())

while 1:
    try:
        port = int(input('Enter port number to run on --> '))
        s.bind((ip, port))
        break
    except:
        print("Couldn't bind to that port")

def broadcast(sock, data):
    for client in connections:
        if client != sock:
            try:
                client.send(data)
            except:
                pass

def handle_client(c,addr):
    while 1:
        try:
            data = c.recv(1024)
            broadcast(c, data)
            
        except socket.error:
            c.close()

def accept_connections():
    s.listen(100)
    print('Running on IP: '+str(ip))
    print('Running on port: '+str(port))
    while True:
        c, addr = s.accept()
        connections.append(c)
        threading.Thread(target=handle_client,args=(c,addr,)).start()

connections = []
accept_connections()

       


