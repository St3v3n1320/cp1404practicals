def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score! Please enter a value between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def determine_score_status(score):
    if score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print('*' * int(score))


def main():
    score = get_valid_score()
    menu = """
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit """

    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score_status(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option. Please choose a valid option from the menu.")

        print(menu)
        choice = input(">>> ").upper()

    print("Thank you for using the program! Goodbye.")

main()
