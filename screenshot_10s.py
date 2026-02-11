import pyautogui
import time
import os
from datetime import datetime

interval = 300
folder = "periodic_screenshots"
os.makedirs(folder, exist_ok=True)

print("Running... to stop.")

try:
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        path = os.path.join(folder, f"{timestamp}.png")
        
        screenshot = pyautogui.screenshot()
        screenshot.save(path)

        print(f"Saved {path}")
        time.sleep(interval)

except KeyboardInterrupt:
    print("Stopped.")