import random

NUM_IN_EACH_LINE = 6
line_num = int(input("How many quick picks? "))

for row in range(line_num):
    line_numbers = sorted(random.sample(range(1, 46), NUM_IN_EACH_LINE))
    for number in line_numbers:
        print(f"{number:2}", end=" ")
    print()