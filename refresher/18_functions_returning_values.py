def add(x, y):
    return x + y

print(add(5, 3))

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return 'You fool!'

result = divide(15, 3)
print(result)