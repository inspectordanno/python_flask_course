class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #called when you want to turn your object into a string
    def __str__(self):
        return f"Person {self.name}, {self.age} years old."

    #used to print out an unambiguous representation of an object
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

bob = Person('Bob', 35)
print(bob)