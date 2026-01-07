import time
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt


def x():
    while True:
        try:
            # cast to float
            a = float(input("Please enter a number between 1 and 0: "))      # check it is in the correct
            # range and is so return
            if 0 <= a <= 1:
                return a
            # else tell user they are not in the correct range
            print("Please try again, it must be a number between 0 and 1")
        except ValueError:
            # got something that could not be cast to a float
            print("Input must be numeric.")


start_time = time.time()

n = int(input("Enter Number of flips: "))  # Number of trials
p = x()  # Probability of success (getting heads)
size = int(input("Enter number of trials: "))  # Number of trials

# Simulate flipping the coin
num_heads = np.random.binomial(n, p, size)

# Plot the resulting probability mass on a histogram
# pd.DataFrame(num_heads).hist(range=(-0.5, 10.5), bins=11)

plt.hist(num_heads, range=(-0.5, n+0.5), bins=n+1, density=True)
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title(f"Probability Mass of Flipping a Fair Coin {n} Times")

print(pd.crosstab(index="counts", columns=num_heads))
print("--- %s seconds ---" % (time.time() - start_time))

plt.show()
