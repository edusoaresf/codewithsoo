def palindrome(word):
    reversed_word = word[::-1]
    
    print(f'"{word}" is a palindrome!') if reversed_word.lower() == word.lower() else print(f'{word} is not a palindrome.')

word = input('Type a word: ')
word = word.replace(" ", "")

try:
    word = str(word)
except ValueError:
    print('Type a word.')

if len(word) > 2:
    palindrome(word)
else:
    print('The entered word has no more than 2 characters.')