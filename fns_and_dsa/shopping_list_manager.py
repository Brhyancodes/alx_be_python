# shopping_list_manager.py

shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f"Added {item} to the shopping list.")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed {item} from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

def display_list():
    if shopping_list:
        print("Current Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("The shopping list is empty.")

#  display_menu() 
def display_menu():
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    while True:
        display_menu()  

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == '3':
            display_list()
        elif choice == '4':
            print("Exiting the Shopping List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
