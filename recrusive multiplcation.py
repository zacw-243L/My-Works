def multiply(a, b):
    if b == 0:
        return 0
    return a + multiply(a, b - 1)


def multiply2(a, b):
    if b == 0:
        return 0
    if b > 0:
        return a + multiply2(a, b - 1)
    return -multiply2(a, -b)  # Handle negative b


# x = multiply2(3, 4)  # 12
y = multiply2(1, -1)

# x = multiply(3, 4)  # 12
# y = multiply(1, -1)
print(y)
