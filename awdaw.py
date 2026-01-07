import numpy as np
import pandas as pd

F = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(F)
print(np.ndim(F))
print(np.shape(F))
print(F[1::2, 1:3])

print(F[0:4, 1::2])

# Create an (8,8) 2D array of ones with data type=integer
Z = np.full((8, 8), 1, dtype=np.int32)

# Print the array
print(Z)

# Create the numpy array D
D = np.full((8, 8), 0, dtype=np.int32)

# Set the border elements to 1
D[0, :] = 1
D[-1, :] = 1
D[:, 0] = 1
D[:, -1] = 1

# Print the modified array
print(D)

df1 = pd.DataFrame({'Name': ['Axel', 'Alice', 'Alex'], 'Age': [32, 16, 26]})
df1["Weight"] = [60, 50, 70]
print(df1)


df = pd.read_csv('https://raw.githubusercontent.com/seowbk/data/main/gapminder.tsv', sep='\t')
print(df.head())
