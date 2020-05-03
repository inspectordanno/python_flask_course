def hello():
    print('hello')

hello()

def user_age_in_seconds():
    user_age = int(input('Enter your age: '))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f'Your age in seconds in {age_seconds}.')

user_age_in_seconds()

# don't do this - shadowing variables from global scope

friends = 'rolf'

def add_friend():
    friend_name = input('enter your friend name: ')
    friends = friends + friend_name

add_friend()