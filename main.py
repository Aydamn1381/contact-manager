import json


def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)


contacts = load_contacts()


def validate_number(number):
    return number.isdigit() and len(number) == 11 and number.startswith("09")


def validate_email(email):
    return "@" in email and "." in email


def add_contact():
    while True:
        name = input("Enter name:")

        if name.strip():
            break

        print("Name cannot be empty!")

    while True:
        number = input("Enter number:")

        if not validate_number(number):
            print("Invalid number! Please try again.")
            continue

        if any(contact["number"] == number for contact in contacts):
            print("Number already exists")
            continue

        break

    while True:
        email = input("Enter email:")

        if validate_email(email):
            break

        print("Invalid email! Please try again.")

    contact = {"name": name, "number": number, "email": email}

    contacts.append(contact)
    save_contacts()

    print("Contact added successfully✅")


def display_contact(contact):
    print(f"Name: {contact['name']}")
    print(f"Number: {contact['number']}")
    print(f"Email: {contact['email']}")
    print(f"-----------------------")


def show_contacts():
    if not contacts:
        print("No contacts found")
        return

    print("\n---Contacts---")

    for contact in contacts:
        display_contact(contact)


def search_contact():
    search = input("Enter contact name to search:")
    found = False
    for contact in contacts:
        if search.lower() == contact["name"].lower():
            print("Contact found")
            display_contact(contact)
            found = True
            break
    if not found:
        print("No contacts found")


def edit_contact():
    edit = input("Enter the name you want to edit:")
    found = False

    for contact in contacts:
        if edit.lower() == contact["name"].lower():

            print("---Contact info---")
            display_contact(contact)

            new_name = input("\nNew name (press enter to keep current):")
            new_number = input("New number (press enter to keep current):")
            new_email = input("New email (press enter to keep current):")

            if new_name:
                contact["name"] = new_name

            if new_number:
                if not validate_number(new_number):
                    print("Invalid number! Contact was not updated")
                    return

                number_exists = False

                for c in contacts:
                    if c["number"] == new_number:
                        number_exists = True
                        break

                if number_exists:
                    print("Number already exists!")
                    return

                contact["number"] = new_number

            if new_email:
                if not validate_email(new_email):
                    print("Invalid email! Contact was not updated")
                    return

                contact["email"] = new_email

            save_contacts()

            found = True
            print("Contact updated successfully")
            break

    if not found:
        print("No results found")


def delete_contact():
    delete = input("Enter contact name to delete:")
    found = False
    for contact in contacts:
        if delete.lower() == contact["name"].lower():
            confirm = input(
                f"Are you sure you wanna delete {contact['name']}? (yes/no)"
            )
            if confirm.lower() != "yes":
                print("Delete cancelled")
                return
            contacts.remove(contact)
            save_contacts()
            found = True
            print("Contact deleted successfully✅")
            break
    if not found:
        print("No results found")


def main():
    while True:
        print("\n---Menu---")
        print("1.Add contact")
        print("2.Show contacts")
        print("3.Search contact")
        print("4.Edit contact")
        print("5.Delete contact")
        print("6.Exit")

        choice = input("Choose an option:")

        if choice == "1":
            add_contact()

        elif choice == "2":
            show_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            edit_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("Goodbye!👋")
            break


if __name__ == "__main__":
    main()
