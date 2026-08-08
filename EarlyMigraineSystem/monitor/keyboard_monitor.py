from pynput import keyboard
import time

count = 0
start = time.time()

def on_press(key):
    global count
    count += 1

listener = keyboard.Listener(on_press=on_press)
listener.start()

def get_typing_speed():
    global count, start
    elapsed = time.time() - start
    speed = (count / elapsed) * 60 if elapsed > 0 else 0
    count = 0
    start = time.time()
    return speed