user_emails = {}


def split_name_and_email(email):
    suggested_name = email.split("@")[0]
    confirmation = input(f"Is your name {suggested_name.title()}? (Y/N): ").upper()
    if confirmation == 'Y':
        name = suggested_name
    else:
        name = input("Please enter your name: ")
    user_emails[name] = email


email = input("Email: ")

while email != '':
    split_name_and_email(email)
    email = input("Email: ")

for user_name, user_email in user_emails.items():
    print(f"{user_name} ({user_email})")