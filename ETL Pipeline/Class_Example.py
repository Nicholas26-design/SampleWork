# Define a class named "Person"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


# Create an object (instance) of the class
person1 = Person("Alice", 30)

# Access the object's data and methods
print(person1.name)  # Output: Alice (This is accessing the object's data)
print(person1.age)  # Output: 30 (This is accessing the object's data)
print(person1.introduce())  # Output: Hi, I'm Alice and I'm 30 years old. (This is accessing the object's methods)
