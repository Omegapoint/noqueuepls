import sys
import time
import pynput
import guimodule

keyboard = pynput.keyboard

mode = str(sys.argv[1])

shouldRun = False
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
    else:
        print("ALL COORDS SET")
        return False

print(str(coords))


def debug():
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
        moveMouse()
        time.sleep(1000)


def moveMouse(action):
    if action == "PLAY":
        print("HEJ")
    guimodule.moveAndClick(200, 200)
    guimodule.moveAndClick(400, 400)


if mode == "debug":
    debug()
else:
    scheduled()
