from typing import List, Optional

# only use immutable default parameters like integers, strings, tuples, etc.

def __init__(self, name: str, grades: List[int] = []): # bad idea
    pass

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []
    
    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
rolf.take_exam(85)
print(bob.grades)

