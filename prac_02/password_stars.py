password = input("Enter your password: ")
count = 0
for i in password:
    count += 1
for asterisks in range(count):
    print('*', end="")