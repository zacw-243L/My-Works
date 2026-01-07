import random


def hello_world_1():
    print("Hello, World!")


def hello_world_2():
    message = "Hello, World!"
    print(message)


def hello_world_3():
    parts = ["Hello", ", ", "World", "!"]
    print("".join(parts))


def hello_world_4():
    chars = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
    print("".join(chr(c) for c in chars))


def hello_world_5():
    print("H" + "e" + "l" + "l" + "o" + ", " + "W" + "o" + "r" + "l" + "d" + "!")


def choose_hello_world():
    funcs = [hello_world_1, hello_world_2, hello_world_3, hello_world_4, hello_world_5]
    random.choice(funcs)()


choose_hello_world()
