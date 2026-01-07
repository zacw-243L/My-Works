import time
import random
import matplotlib.pyplot as plt

start_time = time.time()

# Define the number of rolls and the sides of the die
num_rolls = 100000
sides = 20

# Initialize a dictionary to store the results
results = {i: 0 for i in range(1, sides+1)}

# Perform the rolls
for _ in range(num_rolls):
    roll = random.randint(1, sides)
    results[roll] += 1

# Prepare data for plotting
rolls = list(results.keys())
counts = list(results.values())

for roll, count in results.items():
    print(f"Roll: {roll}, Count: {count}, Probability: {count/num_rolls}")

# Create the plot
plt.bar(rolls, counts, color='red')
plt.xlabel('Roll')
plt.ylabel('Count')
plt.title('Distribution of Rolls in a D20 Simulation')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
