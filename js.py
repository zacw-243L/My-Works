import math


def calculate_sample_size(population_size, population_mean, population_std_dev, confidence_level, margin_of_error):
    # Calculate the critical value
    z_critical = 0
    if confidence_level == 90:
        z_critical = 1.645
    elif confidence_level == 95:
        z_critical = 1.96
    elif confidence_level == 99:
        z_critical = 2.576
    else:
        raise ValueError("Invalid confidence level. Please choose 90, 95, or 99.")

    # Calculate the minimum sample size
    sample_size = math.ceil((z_critical ** 2 * population_std_dev ** 2) / margin_of_error ** 2)

    return sample_size


# Given values
population_size = 10000
population_mean = 50.0
population_std_dev = 30.0
confidence_level = 95
margin_of_error = 10

# Calculate the minimum sample size
sample_size = calculate_sample_size(population_size, population_mean, population_std_dev, confidence_level,
                                    margin_of_error)

print(f"The minimum sample size required is: {sample_size}")
