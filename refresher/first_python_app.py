user_age = int(input("Enter your age: "))
months = user_age * 12
days = 30
hours = 24
minutes = 60
seconds = 60
age_seconds = months * days * hours * minutes * seconds

print(f"Your age is {user_age}, is equal to {months} months.")
print(f"Your age is {user_age}, is equal to {age_seconds} seconds.")