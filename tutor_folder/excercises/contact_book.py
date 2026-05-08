#contacts book

contacts = {
    "Zion": "09123809756",
    "Alice": "08123456789",
    "Bob": "08098765432",
    "John Doe": "07012345678"
    }

name = input("Enter the name of the contact: ")

print("Phone number:", contacts.get(name, "Contact not found"))