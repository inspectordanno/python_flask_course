add = lambda x, y: x + y

print(add(5, 7))

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubledComprehension = [double(x) for x in sequence] # list comprehensions are usually used over map
doubledMap = list(map(double, sequence)) # map is easier for people coming from other programming languages to understand
doubledLambdaMap = list(map(lambda x: x * 2, sequence)) # use lamba functions with map

print(doubledMap)