#!/usr/bin/env python
import random
import socket, select
from time import gmtime, strftime
from random import randint
#client side code to send image to server
def send_image(img_name):
    image = img_name

    HOST = 'ec2-52-14-210-153.us-east-2.compute.amazonaws.com'
    PORT = 6666

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, PORT)
    sock.connect(server_address)

    try:
        myfile = open(image, 'rb')
        bytes = myfile.read()
        size = len(bytes)

        sock.sendall("SIZE %s" % size)
        answer = sock.recv(4096)


        if answer == 'GOT SIZE':
            sock.sendall(bytes)

            answer = sock.recv(4096)

            if answer == 'GOT IMAGE' :
                sock.sendall("BYE BYE ")
        myfile.close()

    finally:
        sock.close()