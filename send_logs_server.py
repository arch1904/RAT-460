import socket                  

#Receive Log Files Server Side
def receive_log():

    s = socket.socket()             
    host = "ec2-52-14-210-153.us-east-2.compute.amazonaws.com"  
    port = 50000                     

    s.connect((host, port))
    s.send("Hello server!")

    with open('received_file', 'wb') as f:
        while True:
            print('receiving data...')
            data = s.recv(1024)
            print('data=%s', (data))
            if not data:
                break
            # write data to a file
            f.write(data)

    f.close()
    s.close()
