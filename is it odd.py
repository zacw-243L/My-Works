'''def has_odd_number_of_words(string):
    """
    Check if the given string has an odd number of words.
    :param string: The input string.
    :return: True if the string has an odd number of words, False otherwise.
    """
    words = string.split()
    return len(words) % 2 != 0


# Example usage
print(has_odd_number_of_words("Python is a programming language"))  # Output: False
print(has_odd_number_of_words("Hello World!"))  # Output: True
print(has_odd_number_of_words("xx xx"))
print(has_odd_number_of_words("xx xx xx"))'''


def _(_):
    return len(_.split()) % 2 != 0


# Example usage
i = input("Enter a string: ")
if not _(i):
    m = "Sorry, you have been banned!"
    print(m)
else:
    print("You are allowed to enter!")
