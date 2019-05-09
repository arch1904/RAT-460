import socket                  

#Send Log File Client Side
def send_log():
   port = 50000                    
   s = socket.socket()            
   host = "ec2-52-14-210-153.us-east-2.compute.amazonaws.com"   
   s.bind((host, port))            
   s.listen(5)                     


   while True:
      conn, addr = s.accept()     
      data = conn.recv(1024)

      filename='log.txt' 
      f = open(filename,'rb')
      l = f.read(1024)
      while (l):
         conn.send(l)
         l = f.read(1024)
      f.close()
      conn.send('Thank you for connecting')
      conn.close()