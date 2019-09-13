from subprocess import call
import os

def take_screenshot():
    name = "wowqueue.jpg"
    call(["screencapture", name])
    return name

def delete_screenshot(name):
    os.remove(name)
    print("removed screenshot")
