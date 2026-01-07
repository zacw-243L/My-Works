import keyboard  # Make sure to install this module using 'pip install keyboard'

# Create a long list filled with rubbish data
rubbish_data = [f"Item {i}" for i in range(1, 10001)]  # Adjust the range for the desired length


def find_data(data_list, user_input):
    if user_input in data_list:
        index = data_list.index(user_input)
        result = []
        for i in range(index - 2, index + 3):
            if 0 <= i < len(data_list):
                result.append(data_list[i])
            else:
                result.append(None)  # To handle out of range indices
        return result
    else:
        return ["Data not found in list."]


# Main loop
print("Enter data to search for or press 'Esc' to exit.")

while True:
    if keyboard.is_pressed('esc'):
        print("Exiting program.")
        break

    user_input = input("Enter the data to search for: ")
    result = find_data(rubbish_data, user_input)

    if len(result) == 5:
        print("-2:", result[0])
        print("-1:", result[1])
        print("User input:", result[2])
        print("+1:", result[3])
        print("+2:", result[4])
    else:
        print(result[0])
