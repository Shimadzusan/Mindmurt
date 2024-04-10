class ObjectOne:
    # Constructor to initialize the object with name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display information about the person
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
