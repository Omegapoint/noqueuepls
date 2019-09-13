import pyautogui
import os
import base64

def take_screenshot():
    name = "wowqueue.png"
    pyautogui.screenshot(name)
    image = ""
    with open("./testpic.png", "rb") as f:
        data = f.read()
        image = base64.b64encode(data)
    return image

def delete_screenshot(name):
    os.remove(name)
    print("removed screenshot")

take_screenshot()
