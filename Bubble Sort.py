import matplotlib.pyplot as plt
import numpy as np
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                plt.bar(x, arr)
                plt.pause(0.01)
                plt.clf()
    return arr


amount = 100
lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

start_time = time.time()
sorted_lst = bubble_sort(lst)
print("--- %s seconds ---" % (time.time() - start_time))

plt.bar(x, sorted_lst)
plt.show()
