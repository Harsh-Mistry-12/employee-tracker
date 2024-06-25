from pynput.keyboard import Listener

keypress_count = 0

def on_press(key):
    global keypress_count
    keyClicks = []
    keypress_count += 1
    keyClicks.append(keypress_count)
    print(keyClicks[-1])

with Listener(on_press=on_press) as listener:
    listener.join()
