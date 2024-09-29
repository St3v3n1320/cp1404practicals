# a

for i in range(0, 101, 10):
    print(i, end=' ')

# b

for i in range(20, 0, -1):
    print(i, end=' ')

# c

star_num = int(input("Number of stars: "))
for i in range(star_num):
    print("*", end="")

# d
star_num = int(input("Number of rows: "))
for i in range(star_num):
    for j in range(i +1):
        print("*", end="")
    print()

