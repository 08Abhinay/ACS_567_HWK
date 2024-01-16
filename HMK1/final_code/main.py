# main.py
from datamanager import DataManager
from applicationdriver import ApplicationDriver

# Example usage
user_filename = input("Enter the filename: ")
data_manager = DataManager(user_filename)

# Menu loop
while True:
    print("\nMenu:")
    print("1. Display Data")
    print("2. List Available Files")
    print("3. Filter Data")
    print("4. CRUD Operations")
    print("5. Calculate Mean")
    print("6. Calculate Median")
    print("7. Exit")

    menu_choice = input("Enter your choice (1/2/3/4/5): ")

    if menu_choice == '1':
        data_manager.data.display_data()
    elif menu_choice == '2':
        ApplicationDriver.list_files()
    elif menu_choice == '3':
        ApplicationDriver.filter_data(data_manager)
    elif menu_choice == '4':
        # Ask the user for CRUD operation choice
        while True:
            print("\nChoose CRUD operation:")
            print("1. Add Data")
            print("2. Edit Data")
            print("3. Delete Data")
            print("4. Back to Main Menu")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == '1':
                new_element = int(input("Enter the new element to add: "))
                data_manager.data.add_data(new_element)
            if choice == '2':
                index_to_edit = int(input("Enter the index to edit: "))
                new_value = int(input("Enter the new value: "))
                data_manager.data.edit_data(index_to_edit, new_value)
            elif choice == '3':
                index_to_delete = int(input("Enter the index to delete: "))
                data_manager.data.delete_data(index_to_delete)
            elif choice == '4':
                print("Returning to Main Menu.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
    elif menu_choice == '5':
        print("Mean:", data_manager.data.mean())
    elif menu_choice == '6':
        print("Median:", data_manager.data.median())
    elif menu_choice == '7':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6 or 7.")
