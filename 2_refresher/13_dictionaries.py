friend_ages = {'Rolf': 24, 'Adam': 30, 'Anne': 27}

print(friend_ages['Adam'])

friend_ages['Rolf'] = 40

print(friend_ages)

friends = [
    {'name': 'Rolf', 'age': 24},
    {'name': 'Anne', 'age': 22},
    {'name': 'Bob', 'age': 23}
]

print(friends[1]["name"])

# iterate over a dictionary
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# check if key is in dictionary
if 'Bob' in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print('Bob is not a student in this class.')

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))

attendance_keys = student_attendance.keys()
print(attendance_keys)