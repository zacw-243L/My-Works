import matplotlib.pyplot as plt
import numpy as np
import time


def is_sorted(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True


def bogosort(arr):
    while not is_sorted(arr):
        np.random.shuffle(arr)
        plt.bar(x, arr)
        plt.pause(0.01)
        plt.clf()
    return arr


amount = 10
lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

start_time = time.time()
sorted_lst = bogosort(lst)
print("--- %s seconds ---" % (time.time() - start_time))

plt.bar(x, sorted_lst)
plt.show()
