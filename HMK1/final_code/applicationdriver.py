# applicationdriver.py
import os

class ApplicationDriver:
    @staticmethod
    def list_files():
        files = [f for f in os.listdir() if os.path.isfile(f)]
        print("Available Files:", files)

    @staticmethod
    def filter_data(data_manager):
        print("\nChoose filter type:")
        print("1. Greater Than")
        print("2. Less Than")
        print("3. Equal To")
        print("4. Range (Between two values)")
        print("5. Specific Values")

        filter_choice = input("Enter your filter choice (1/2/3/4/5): ")

        try:
            filter_choice = int(filter_choice)
            if filter_choice in [1, 2, 3, 4, 5]:
                if filter_choice in [1, 2, 3]:
                    filter_value = int(input("Enter the filter value: "))
                elif filter_choice == 4:
                    filter_start = int(input("Enter the start of the range: "))
                    filter_end = int(input("Enter the end of the range: "))
                elif filter_choice == 5:
                    specific_values = input("Enter specific values separated by commas: ").split(',')
                    specific_values = [int(value) for value in specific_values]

                if filter_choice == 1:
                    filtered_data = [value for value in data_manager.data.data if value > filter_value]
                elif filter_choice == 2:
                    filtered_data = [value for value in data_manager.data.data if value < filter_value]
                elif filter_choice == 3:
                    filtered_data = [value for value in data_manager.data.data if value == filter_value]
                elif filter_choice == 4:
                    filtered_data = [value for value in data_manager.data.data if filter_start <= value <= filter_end]
                elif filter_choice == 5:
                    filtered_data = [value for value in data_manager.data.data if value in specific_values]

                print("Filtered Data:", filtered_data)
            else:
                print("Invalid filter choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
