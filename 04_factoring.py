def factorial(number):
    result = 1
    print(f'{number}! =', end=' ')
    for i in range(1, number + 1):
        result *= i
    return print(result)

number = input('Enter the number: ')
number = number.replace(' ', '')

try:
    number = int(number)
except ValueError:
    print('Invalid value.')
else:
    factorial(number)
