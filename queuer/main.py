import sys
import time
import pynput
import guimodule
import json

keyboard = pynput.keyboard

mode = ""

shouldRun = False

try:
    mode = str(sys.argv[1])
except:
    print("Regular mode")
    shouldRun = True

coords = {}

try:
    with open('coords.json') as json_file:
        coords = json.load(json_file)
except:
    coords = {
        "PLAY": (0, 0),
        "CHOOSE_SERVER": (0, 0),
        "CHANGE_REALM": (0, 0),
        "CANCEL": (0, 0),
        "QUIT": (0, 0)
    }


def on_press(key):
    try:
        # print('alphanumeric key {0} pressed'.format(
        #     key.char))
        if key.char == '1':
            x, y = guimodule.getMousePosition()
            coords["PLAY"] = (x, y)
            print(str(coords))
        if key.char == '2':
            x, y = guimodule.getMousePosition()
            coords["CHOOSE_SERVER"] = (x, y)
            print(str(coords))
        if key.char == '3':
            x, y = guimodule.getMousePosition()
            coords["CHANGE_REALM"] = (x, y)
            print(str(coords))
        if key.char == '4':
            x, y = guimodule.getMousePosition()
            coords["CANCEL"] = (x, y)
            print(str(coords))
        if key.char == '5':
            x, y = guimodule.getMousePosition()
            coords["QUIT"] = (x, y)
            print(str(coords))
    except AttributeError:
        print()


def on_release(key):
    if (0, 0) in list(coords.values()):
        print("CONTINUE SET COORDS")
        with open('coords.json', 'w') as outfile:
            json.dump(coords, outfile)
    else:
        with open('coords.json', 'w') as outfile:
            json.dump(coords, outfile)
        print("ALL COORDS SET. SAVED coords.json")
        print("Restart program with no arguments")
        return False


print(str(coords))


def debug():
    global coords

    coords = {
        "PLAY": (0, 0),
        "CHOOSE_SERVER": (0, 0),
        "CHANGE_REALM": (0, 0),
        "CANCEL": (0, 0),
        "QUIT": (0, 0)
    }
    print("Record coords of following buttons:")
    print("Key 1 = PLAY")
    print("Key 2 = CHOOSE_SERVER")
    print("Key 3 = CHANGE_REALM")
    print("Key 4 = CANCEL")
    print("Key 5 = QUIT")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def scheduled():
    while shouldRun:
        time.sleep(3)
        moveMouse("PLAY")
        time.sleep(8)
        moveMouse("CHOOSE_SERVER")
        time.sleep(10)
        #MAKE GABE SCREENSHOTSTUFF
        moveMouse("CHANGE_REALM")
        time.sleep(2)
        moveMouse("CANCEL")
        time.sleep(2)
        moveMouse("QUIT")
        time.sleep(60)

def moveMouse(action):
    x, y = coords.get(action)
    print("move?")
    guimodule.moveAndClick(x, y)


if mode == "debug":
    debug()
else:
    scheduled()
