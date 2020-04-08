## while loop
# number = 7
# user_input = input("Would you like to play? (Y/n) ")

# while True:
#     if user_input == 'n':
#         break

#     user_number = int(input('Guess our number: '))

#     if user_number == number:
#         print('You guessed correctly!')
#     elif abs(number - user_number) == 1:
#         print('You were off by one.')
#     else:
#         print('Sorry, it is wrong.')

#for loop
friends = ['Rolf', 'Jen', 'Bob', 'Anne']

for friend in friends:
    print(f'{friend} is my friend.')

for i in range(10):
    print(i)

grades= [35, 67, 98, 100, 100]
total = 0
sumTotal = sum(grades)
amount = len(grades)

# find the average
for grade in grades:
    total += grade

print(total / amount)
    

