import time
from pynput.mouse import Listener, Button
from threading import Thread, Event

# Set the desired RPM (rounds per minute)
RPM = 1200
# Calculate the delay between each shot in seconds
delay_between_shots = 60 / RPM

# Event to control the firing thread
firing_event = Event()


def fire():
    while firing_event.is_set():
        print("bang")
        time.sleep(delay_between_shots)


def on_click(x, y, button, pressed):
    if button == Button.left:
        if pressed:
            # Start firing when the left mouse button is pressed
            firing_event.set()
            Thread(target=fire).start()
        else:
            # Stop firing when the left mouse button is released
            firing_event.clear()


# Set up the listener for mouse events
with Listener(on_click=on_click) as listener:
    listener.join()
