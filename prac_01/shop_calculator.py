total = 0
item_num = int(input("Number of items: "))
while item_num < 0:
    print("Invalid number of items!")
    item_num = int(input("Number of items: "))
for i in range(item_num):
    item_price = float(input("Price of item: "))
    total += item_price
print(f"Total price for {item_num} items is ${total}")