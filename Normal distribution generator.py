import time
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

A = float(input("Enter number: "))
B = float(input("Enter number: "))
start_time = time.time()

rv_normal = norm(A, B)
x = np.arange(A-A, A+1.08, 0.01)
plt.figure()
plt.plot(x, rv_normal.pdf(x))
plt.title(f"Probability Density Function (PDF) of X~N( {A}, {B} )")
plt.xlabel('x')
plt.ylabel('f(x)')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
