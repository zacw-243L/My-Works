from pynput.mouse import Listener


def on_click(x, y, button, pressed):
    if button == button.left and pressed:
        print("bang")


# Collect events until released
with Listener(on_click=on_click) as listener:
    listener.join()
