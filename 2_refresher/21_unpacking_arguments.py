def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total


print(multiply(1, 3, 5))

def add(x, y):
    return x + y

#unpacking arguments in list
nums = [3, 5]
print(add(*nums))

#unpacking arguments in dictionary
numDict = { "x": 15, "y": 25}
print(add(**numDict))

#required named argument: operator
def apply(*args, operator):
    if operator == "*":
        return multiply(*args) #unpacking tuple
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(1, 3, 5, 7, operator="*"))
