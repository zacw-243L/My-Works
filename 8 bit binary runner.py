import time
import keyboard

numbers = [1, 2, 4, 8, 16, 32, 64, 128]

def display_binary(number):
    binary = bin(number)[2:].zfill(8)
    print(binary)
    print(" ")

def binary_runner():
    for number in numbers:
        display_binary(number)

while 1:
    start_time = time.time()
    binary_runner()
    if keyboard.on_press.name ==  "esc":
        break

print("--- %s seconds ---" % (time.time() - start_time))