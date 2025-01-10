# Define the all_contact dictionary to store contacts
all_contact = {}

def add_contact(name, number):
    all_contact[name] = number
    # print(f"The contact information is added {name}-{number}")

def view_contact(name1):
    if name1 in all_contact:
        print(all_contact[name1])
        for name, number in all_contact.items():
            print(f"{name} and {number}")
    else:
        print("Contact is not found!")
        
def remove_contact(name):
    if name in all_contact:
        del all_contact[name]
        print(f"The contact is deleted: {name}")
    else:
        print("Contact is not found!")
        
while True:
    print("\nContact Book Menu:")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Remove contact")
    print("4. Quit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter your name: ")
        number = input("Enter your number: ")
        add_contact(name, number)
        print(f"Your data is successfully added: {name} and {number}")
    elif choice == 2:
        name1 = input("Enter name: ")
        view_contact(name1)     
    elif choice == 3:
        name = input("Enter name: ")
        remove_contact(name)
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Enter a valid option!")
