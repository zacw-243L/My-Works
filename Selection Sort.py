import matplotlib.pyplot as plt
import numpy as np
import time


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        plt.bar(x, arr)
        plt.pause(0.01)
        plt.clf()
    return arr


amount = 100
lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

start_time = time.time()
sorted_lst = selection_sort(lst)
print("--- %s seconds ---" % (time.time() - start_time))

plt.bar(x, sorted_lst)
plt.show()
