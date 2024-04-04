months_list = ['January', 'February', 'March',
               'April', 'May', 'June',
               'July', 'August', 'September',
               'Octuber', 'November', 'December']

number = input('Enter the number of a month: ')

number = number.replace(' ', '')

try:
    number = int(number)
except ValueError:
    print('Invalid value.')
else:
    for numberi, month in enumerate(months_list):
        if number > 12 or number < 0:
            print(f"There are no {number} months.")    
            break
        else:
            if number == numberi+1:
                print(f'The month {number} is {month}!')
