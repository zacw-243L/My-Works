def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Division by zero is not allowed")

    # Determine the sign of the result
    sign = -1 if (dividend < 0) != (divisor < 0) else 1
    dividend, divisor = abs(dividend), abs(divisor)

    if dividend < divisor:
        return 0 * sign, dividend if sign > 0 else -dividend  # Quotient, remainder

    quotient, remainder = divide(dividend - divisor, divisor)
    return (quotient + 1) * sign, remainder if sign > 0 else -remainder


# Example usage
try:
    quotient, remainder = divide(100, 3)
    print(f"10 ÷ 3: Quotient: {quotient}, Remainder: {remainder}")  # 3, 1
    quotient, remainder = divide(-10, 3)
    print(f"-10 ÷ 3: Quotient: {quotient}, Remainder: {remainder}")  # -3, -1
    quotient, remainder = divide(10, -3)
    print(f"10 ÷ -3: Quotient: {quotient}, Remainder: {remainder}")  # -3, 1
    quotient, remainder = divide(-20, -3)
    print(f"-10 ÷ -3: Quotient: {quotient}, Remainder: {remainder}")  # 3, -1
except ValueError as e:
    print(e)
