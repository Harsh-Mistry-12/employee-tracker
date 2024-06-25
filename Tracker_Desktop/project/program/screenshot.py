import time
import threading
from PIL import ImageGrab

def capture_and_save_screenshots():
    def capture_and_save_screenshot():
        while True:
            screenshot = ImageGrab.grab()
            filename = f"screenshots/screenshot_{int(time.time())}.png"
            screenshot.save(filename)
            print(f"Screenshot saved: {filename}")
            time.sleep(5)

    screenshot_thread = threading.Thread(target=capture_and_save_screenshot)
    screenshot_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

# Call the function to start the process
capture_and_save_screenshots()
