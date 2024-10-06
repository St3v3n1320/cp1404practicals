# For line 1, 5 is the smallest possible number and 20 is the largest possible number.
# For line 2, 3 is the smallest possible number and 9 is the largest possible number.
# Line 2 could not have produced a 4, because the function only produces numbers
# that are part of the sequence, 3, 5, 7, and 9.
# For line 3, 2.5 is the smallest possible number and 5.5 is the largest possible number.

import random

# Task: Generate a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")