string = input('Enter your word: ')
reversed_str = lambda word: word[::-1]

if not string:
    print('Invalid value.')
else:
    try:
        string = str(string)
    except ValueError:
        print('Invalid value.')
    else:
        print(reversed_str(string))
