string = input('Enter your word: ')
reversal_str = lambda word: word[::-1]

if not string:
    print('Invalid value.')
else:
    try:
        string = str(string)
    except ValueError:
        print('Invalid value.')
    else:
        print(reversal_str(string))