import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()

n = 10  # Number of trials
p = 0.5  # Probability of success (getting heads)

# Simulate flipping the coin 10,000 times
num_heads = np.random.binomial(n, p, size=10000)

# Plot the resulting probability mass on a histogram
# pd.DataFrame(num_heads).hist(range=(-0.5, 10.5), bins=11)
plt.hist(num_heads, range=(-0.5, 10.5), bins=11, density=True)
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('Probability Mass of Flipping a Fair Coin 10 Times')

print(pd.crosstab(index="counts", columns=num_heads))
print("--- %s seconds ---" % (time.time() - start_time))

plt.show()
