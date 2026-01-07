# Importing the required library for standard deviation calculation
import statistics

# Creating a dictionary to map grades to numerical values
grades = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 1,
    'F-': 0
}

# Given data
data = {
    'A': 42,
    'B': 11,
    'C': 7,
    'D': 17,
    'E': 1,
    'F-': 1
}

# Creating a list with numerical grades repeated as per the frequency in the data
grade_list = []
for grade, count in data.items():
    grade_list.extend([grades[grade]] * count)

# Calculating the standard deviation
std_dev = statistics.stdev(grade_list)

# Displaying the standard deviation
print("Standard Deviation of Grades:", std_dev)
