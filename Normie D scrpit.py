import time
import pandas as pd
import scipy.stats as stats

start_time = time.time()

# Define the mean and standard deviation
mean = 3
std_dev = 4

# Create a range of values for x
x = pd.Series(range(0, 7))
# Calculate the PDF for each value of x
pdf_values = stats.norm.pdf(x, mean, std_dev)
# Create a DataFrame to store the values
df = pd.DataFrame({'x': x, 'PDF': pdf_values})
# Print the DataFrame
print(df)
print("--- %s seconds ---" % (time.time() - start_time))
