t = (5, 11)
x, y = t
print(x, y)

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

people = [
    ('Bob', 42, 'Mechanic'), 
    ('James', 24, 'Artist'),
    ('Harry', 32, 'Lecturer')
]

for name, age, profession in people:
    print(f"{name} is {age}, and they are a {profession}")

for name, _, profession in people:
    print(f"{name} is a {profession}")

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)
