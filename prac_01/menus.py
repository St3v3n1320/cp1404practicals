name = input("Enter name: ")
menu = "(H)ello\n(G)oodbye\n(Q)uit"
print(menu)

option = input(">>> ").upper()
while option not in ('H', 'G', 'Q'):
    print("Invalid choice")
    option = input(">>> ").upper()

while option != 'Q':
    if option == 'H':
        print("Hello " + name)
    else:
        print("Goodbye " + name)
    print(menu)
    option = input(">>> ").upper()
print("Finished")