# collects keyword arguments into a dictionary
def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25)



##unpack dictionary into keyword arguments
def namedTwo(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}

namedTwo(**details)

def print_nicely(**kwargs):
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bob", age=25)
