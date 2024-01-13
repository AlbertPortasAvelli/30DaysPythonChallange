class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"

class MainApp:
    def __init__(self):
        self.contacts = []

    def display_menu(self):
        print("\nMenu:")
        print("1. View Contacts")
        print("2. Add New Contact")
        print("3. Search for Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nContacts:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact}")

    def add_contact(self):
        name = input("Enter the name: ")
        email = input("Enter the email: ")
        phone = input("Enter the phone number: ")

        if name and email and phone:
            self.contacts.append(Contact(name, email, phone))
            print("Contact added successfully!")
        else:
            print("Invalid input. Please provide all the required information.")

    def search_contact(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            search_name = input("Enter the name to search: ")
            found_contacts = [contact for contact in self.contacts if search_name.lower() in contact.name.lower()]

            if not found_contacts:
                print("No matching contacts found.")
            else:
                print("\nMatching Contacts:")
                for index, contact in enumerate(found_contacts, start=1):
                    print(f"{index}. {contact}")

    def edit_contact(self):
        self.view_contacts()
        if not self.contacts:
            print("No contacts available.")
            return

        try:
            index = int(input("Enter the index of the contact to edit: ")) - 1
            if 0 <= index < len(self.contacts):
                print("\nEdit Menu:")
                print("1. Edit Full Contact")
                print("2. Edit Specific Attributes")
                choice = input("Enter your choice (1-2): ")

                if choice == '1':
                    new_name = input("Enter the new name: ")
                    new_email = input("Enter the new email: ")
                    new_phone = input("Enter the new phone number: ")
                    self.contacts[index] = Contact(new_name, new_email, new_phone)
                    print("Contact edited successfully!")
                elif choice == '2':
                    self.edit_specific_attributes(index)
                else:
                    print("Invalid choice.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def edit_specific_attributes(self, index):
        print("\nChoose attributes to edit:")
        print("1. Name")
        print("2. Email")
        print("3. Phone")
        edit_choices = input("Enter your choices (e.g., 1 2): ").split()

        for edit_choice in edit_choices:
            if edit_choice == '1':
                self.contacts[index].name = input("Enter the new name: ")
            elif edit_choice == '2':
                self.contacts[index].email = input("Enter the new email: ")
            elif edit_choice == '3':
                self.contacts[index].phone = input("Enter the new phone number: ")
            else:
                print(f"Invalid choice: {edit_choice}")
                break

        print("Contact edited successfully!")

    def delete_contact(self):
        self.view_contacts()
        if not self.contacts:
            print("No contacts available.")
            return

        try:
            index = int(input("Enter the index of the contact to delete: ")) - 1
            if 0 <= index < len(self.contacts):
                deleted_contact = self.contacts.pop(index)
                print(f"Contact deleted successfully:\n{deleted_contact}")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main_app = MainApp()

    while True:
        main_app.display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            main_app.view_contacts()
        elif choice == '2':
            main_app.add_contact()
        elif choice == '3':
            main_app.search_contact()
        elif choice == '4':
            main_app.edit_contact()
        elif choice == '5':
            main_app.delete_contact()
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
