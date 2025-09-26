# Create a Python script named shopping_list_manager.py that implements a simple interface for managing a shopping list
# Script should start with an empty list named shopping_list


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item = input("What would you like to add? ")
            shopping_list.append(add_item)
        elif choice == '2':
            remove_item = input("What would you like to remove? ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
            else:
                print(f"{remove_item} not in the list")
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
