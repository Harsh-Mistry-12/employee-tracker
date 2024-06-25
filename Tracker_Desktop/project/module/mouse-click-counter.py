from pynput.mouse import Listener

# Initialize click counter
click_count = 0

def on_click(x, y, button, pressed):
    global click_count
    totalClicks = []
    if pressed:
        click_count += 1
        totalClicks.append(click_count)
        print(totalClicks[-1])

# Start listening to mouse clicks
with Listener(on_click=on_click) as listener:
    listener.join()
