import mss
import mss.tools
import os
from PIL import Image
import io
import keyboard

print("Welcome to screenclipper, this program will clip from your 3rd monitor, it's scaled and made for site assessment photos.")
def capture_screenshot():
    with mss.mss() as sct:
        sct_img = sct.grab(monitor_region)
        screenshot = mss.tools.to_png(sct_img.rgb, sct_img.size)
        return screenshot

def save_screenshot(screenshot, file_name):
    screenshot = Image.open(io.BytesIO(screenshot))

    # Crop the screenshot
    width, height = screenshot.size
    left = width * 0.20
    top = height * 0.10
    right = width * 0.80
    bottom = height * 0.95
    cropped_screenshot = screenshot.crop((left, top, right, bottom))

    # Save the cropped screenshot to the downloads folder
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    screenshot_path = os.path.join(downloads_path, file_name)
    cropped_screenshot.save(screenshot_path)

    print(f"Cropped screenshot saved to {screenshot_path}")

# Define the monitor to capture
monitor = 2  # Monitor 2 is the third monitor in the setup

# Get the position and size of the monitor
with mss.mss() as sct:
    monitor_list = sct.monitors
    monitor_info = monitor_list[monitor]
    monitor_left = monitor_info["left"]
    monitor_top = monitor_info["top"]
    monitor_width = monitor_info["width"]
    monitor_height = monitor_info["height"]
    monitor_region = {"left": monitor_left, "top": monitor_top, "width": monitor_width, "height": monitor_height}

screenshot_counter = 1

while True:
    # Wait for CTRL + Y to be pressed
    if keyboard.is_pressed('ctrl+y'):
        screenshot = capture_screenshot()
        save_screenshot(screenshot, f"screenshot_{screenshot_counter}.png")
        screenshot_counter += 1
    elif keyboard.is_pressed('ctrl+q'):
        print("Exiting program...")
        break