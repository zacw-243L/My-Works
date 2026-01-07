import random


def encode_message(message):
    shift = random.randint(1, 25)
    encoded = ''.join(chr((ord(char) + shift - 32) % 95 + 32) for char in message)
    return encoded, shift


def decode_message(encoded, shift):
    decoded = ''.join(chr((ord(char) - shift - 32) % 95 + 32) for char in encoded)
    return decoded


# Encode "Hello, World!" differently each time
message = "Hello, World!"
encoded_message, shift = encode_message(message)
print(f"Encoded: {encoded_message}")
print(f"Decoded: {decode_message(encoded_message, shift)}")
