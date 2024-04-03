def primenumber(number):
    if number == 2:
        return 'This number is prime.'

    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return 'This number is not prime.'
        return 'This number is prime.'
    else:
        return 'This number is not prime.'

number0 = input('Type a number: ')

try:
    number0 = int(number0)
except ValueError:
    print('The operation could not be performed because you did not enter a valid value.')
else:
    print(primenumber(number0))

print('-====== END ======-')
