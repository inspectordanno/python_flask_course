# collects keyword arguments into a dictionary
def named(**keyword_args):
    print(keyword_args)

named(name="Bob", age=25)



##unpack dictionary into keyword arguments
def namedTwo(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}

namedTwo(**details)

def print_nicely(**keyword_args):
    for arg, value in keyword_args.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bob", age=25)
