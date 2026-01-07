import time


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    n = int(input("Enter value: "))
    start_time = time.time()
    factorial(n)
    # print(f"{n}! = {result}")
    print("--- %s seconds ---" % (time.time() - start_time))


main()
