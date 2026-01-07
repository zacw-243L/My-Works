import time
from pynput.mouse import Listener, Button
from threading import Thread, Event

# Set the desired RPM (rounds per minute)
RPM = 2400
# Calculate the final delay between each shot in seconds
final_delay_between_shots = 60 / RPM

# Time it takes to reach the desired RPM
wind_up_time = 5  # in seconds

# Event to control the firing thread
firing_event = Event()


def fire():
    start_time = time.time()

    while firing_event.is_set():
        elapsed_time = time.time() - start_time

        # Calculate the new delay based on elapsed time
        if elapsed_time < wind_up_time:
            # Gradually reduce delay, using a linear interpolation
            current_delay = final_delay_between_shots * (1 - (elapsed_time / wind_up_time)) + (wind_up_time - elapsed_time) / 100
        else:
            # Maintain the final delay after wind-up time
            current_delay = final_delay_between_shots

        print("bang")
        time.sleep(current_delay)


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
