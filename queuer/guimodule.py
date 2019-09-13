import pyautogui as mouse


def moveAndClick(x, y):
    mouse.moveTo(x, y, duration=1)


def getMousePosition():
    return mouse.position()
