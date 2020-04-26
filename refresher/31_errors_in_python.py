def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor

grades: list = []

print("Welcome to the average grade program")

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")
else: # if no error happened
     print(f"The average grade is {average}.") 
finally: # will prevent regardless of error
    print("Always prints.")