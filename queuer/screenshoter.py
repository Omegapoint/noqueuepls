import pyautogui
import os
import base64

def take_screenshot():
    name = "wowqueue.jpg"
    pyautogui.screenshot(name)
    with open("./wowqueue.jpg", "rb") as f:
        data = f.read()
        print (base64.b64encode(data))
    return name

def delete_screenshot(name):
    os.remove(name)
    print("removed screenshot")

take_screenshot()
