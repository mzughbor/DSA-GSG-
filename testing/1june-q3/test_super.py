class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, my name is {self.name}.")
    
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name) # Calling constructor of the parent class
        self.student_id = student_id
    
    def show_id(self):
        print(f"My ID is {self.student_id}.")

    def greet(self):
        super().greet() # Calling method from the parent class
        print("I am also a student.")

# Usage
s = Student("Alice", "S123")
s.greet()
# Accessing parent method
s.show_id()
# Accessing subclass method
print(s.name)
# Accessing data member from parent class

#Example: Multilevel Inheritance
class Grandparent:
    def house(self):
        print("Grandparent's house")
class Parent(Grandparent):
    def car(self):
        print("Parent's car")
class Child(Parent):
    def bike(self):
        print("Child's bike")

# Usage
c = Child()
c.house()
c.car()
c.bike()