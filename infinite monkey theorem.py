import random
import time
import string

# Load the complete works of William Shakespeare from a text file
with open('shakespeare_complete_works.txt', 'r') as f:
    target_text = f.read()

print("Number of letters in shakespeare_complete_works.txt:", len(target_text))

start_time = time.time()
attempt = 0
while True:
    generated_text = ''.join(random.choice(string.printable) for _ in range(len(target_text)))
    attempt += 1
    print(f"Attempt {attempt}: {generated_text[:len(target_text)]}...")
    if generated_text == target_text:
        break
    print("Still trying...")
print("Complete works of William Shakespeare generated!")
print("--- %s seconds ---" % (time.time() - start_time))
