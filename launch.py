import ObjectOne
import HttpRequest
import Mindmurt

print("Hello, World!")
# Creating an object of the Person class
objectOne = ObjectOne.ObjectOne("Alice", 30)
objectOne_2 = ObjectOne.ObjectOne("Max", 40)

# Accessing the object's attributes
print(objectOne.name)  # Output: Alice
print(objectOne.age)   # Output: 30

# Calling the object's method to display information
objectOne.display_info()  # Output: Name: Alice, Age: 30
objectOne_2.display_info()  # Output: Name: Alice, Age: 30

customRequest = HttpRequest.HttpRequest()
subject = Mindmurt.Mindmurt()