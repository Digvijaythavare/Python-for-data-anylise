import json
import os
import getpass

FILE_NAME = "passwords.json"


def load_passwords():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


def save_passwords(passwords):
    with open(FILE_NAME, "w") as file:
        json.dump(passwords, file, indent=4)


def add_password(passwords):
    website = input("Website: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    passwords[website] = {
        "username": username,
        "password": password
    }

    save_passwords(passwords)
    print("✅ Password saved successfully!")


def view_passwords(passwords):
    if not passwords:
        print("No passwords saved.")
        return

    for website, details in passwords.items():
        print("\nWebsite :", website)
        print("Username:", details["username"])
        print("Password:", details["password"])


def search_password(passwords):
    website = input("Enter website to search: ")

    if website in passwords:
        print("\nWebsite :", website)
        print("Username:", passwords[website]["username"])
        print("Password:", passwords[website]["password"])
    else:
        print("❌ Website not found.")


def main():
    passwords = load_passwords()

    while True:
        print("\n===== PASSWORD MANAGER =====")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_password(passwords)

        elif choice == "2":
            view_passwords(passwords)

        elif choice == "3":
            search_password(passwords)

        elif choice == "4":
            print("Goodbye! 👋")
            break

        else:
            print("❌ Invalid choice")


main()