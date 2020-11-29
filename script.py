import random

print('Random Number Generator')

min_number = int(input('Input min number: '))

max_number = int(input('Input max number: '))

if min_number >= 0:
    result = random.randint(min_number, max_number)
    print('Random number: ' + str(result))
else:
    print('Number not valid')
