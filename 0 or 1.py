def user_input():
    while True:
        try:
            # cast to float
            initial_input = float(input("Please enter a number between 1 and 0"))  # check it is in the correct
            # range and is so return
            if 0 <= initial_input <= 1:
                return initial_input
            # else tell user they are not in the correct range
            print("Please try again, it must be a number between 0 and 1")
        except ValueError:
            # got something that could not be cast to a float
            print("Input must be numeric.")


user_input()
