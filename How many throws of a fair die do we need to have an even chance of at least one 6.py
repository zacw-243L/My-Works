import random


def simulate_dice_throws():
    num_throws = 0
    while True:
        num_throws += 1
        roll = random.randint(1, 6)
        if roll == 6:
            return num_throws


# Simulate many times to get an average
num_simulations = 100000
total_throws = sum(simulate_dice_throws() for _ in range(num_simulations))

average_throws = total_throws / num_simulations
print(f"Average number of throws needed: {average_throws}")
