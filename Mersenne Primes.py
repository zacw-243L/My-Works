import time
import gmpy2

gmpy2.get_context().precision = 200  # Set the precision to 200 bits


def is_prime(n):
    return gmpy2.is_prime(n)


def is_mersenne_prime(p):
    mersenne = gmpy2.mpz(2) ** p - 1
    start_time = time.time()
    is_prime_result = is_prime(mersenne)
    end_time = time.time()
    calculation_time = end_time - start_time
    return is_prime_result, calculation_time


limit = int(input("Enter a limit: "))

mersenne_prime_count = 0  # Initialize counter for Mersenne primes

for p in range(2, limit + 1):
    if is_prime(p):
        print(f"\rChecking Mersenne number 2^{p} - 1...", end="", flush=True)
        result, time_taken = is_mersenne_prime(p)
        if result:
            mersenne_prime_count += 1
            print(f"\nThe Mersenne number 2^{p} - 1 is a prime number.")
            print(f"This is Mersenne prime: {mersenne_prime_count}")
            print("Calculation took %s seconds.\n" % time_taken)
