import sys
import time

string = ""


def addChar(symbol):
    global string
    for i in range(31, 128):
        sys.stdout.write("\r" + string + chr(i))
        sys.stdout.flush()
        time.sleep(0.02)  # speed of flip animation
        if chr(i) == symbol:
            string += symbol
            return


for c in "Hello World!":
    addChar(c)

print()  # move to new line after finishing
