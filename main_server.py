import subprocess
import receive_image
import send_logs_server
from threading import Thread
## main server side initiates all required processes 

if __name__ == "__main__":
    subprocess.Popen(["python3","server.py"])
    thread = Thread(target = receive_image.receive_image, args=None)
    thread2 = Thread(target = send_logs_server.receive_log, args=None)
    thread.start()
    thread2.start()
    thread.join()
    thread2.join()