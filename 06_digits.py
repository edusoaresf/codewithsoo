def count_digits(number):
    print(f'{number} has {len(number)} digits.')

number = input('Enter a number: ')
number = number.replace(" ", "")

try:
    number = int(number)
except ValueError:
    print('Invalid value.')
else:
    number = str(number)
    count_digits(number)