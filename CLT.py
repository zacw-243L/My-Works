import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

numIterations = np.asarray([1, 2, 5, 10, 50, 100])  # number of i.i.d RVs
experiment = 'dice'  # valid values: 'dice', 'coins'
maxNumForExperiment = {'dice': 6, 'coins': 2}  # max numbers represented on dice or coins
nSamp = 100000

k = maxNumForExperiment[experiment]

fig, fig_axes = plt.subplots(ncols=3, nrows=2, constrained_layout=True)

for i, N in enumerate(numIterations):
    y = np.random.randint(low=1, high=k + 1, size=(N, nSamp)).sum(axis=0)
    row = i // 3
    col = i % 3
    bins = np.arange(start=min(y), stop=max(y) + 2, step=1)
    fig_axes[row, col].hist(y, bins=bins, density=True)
    fig_axes[row, col].set_title('N={} {}'.format(N, experiment))
plt.show()
