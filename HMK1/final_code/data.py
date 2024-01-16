# data.py

class Data:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_data()

    def read_data(self):
        with open(self.filename, 'r') as file:
            data = file.read().split(',')
        # Convert strings to integers
        data = [int(value) for value in data]
        return data

    def write_data(self):
        # Convert integers to strings
        data_str = ','.join(map(str, self.data))
        with open(self.filename, 'w') as file:
            file.write(data_str)

    def add_data(self, new_element):
        if new_element in self.data:
            raise ValueError("Duplicate values are not allowed.")
        else:
            self.data.append(new_element)
            self.write_data()
            print("Data added successfully.")

    def edit_data(self, index, new_value):
        if new_value in self.data and self.data.index(new_value) != index:
            raise ValueError("Duplicate values are not allowed.")
        else:
            self.data[index] = new_value
            self.write_data()
            print("Data edited successfully.")

    def delete_data(self, index):
        del self.data[index]
        self.write_data()

    def display_data(self):
        print("Current Data:", self.data)
        
    def mean(self):
        if not self.data:
            return 0
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]
