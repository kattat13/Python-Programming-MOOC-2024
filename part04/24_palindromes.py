# Write your solution here
def palindromes(word: str):
    if ''.join(reversed(word)) == word:
        return True
    return False


while True:
    user = input('Please type in a palindrome: ')
    if palindromes(user):
        print(f'{user} is a palindrome!')
        break
    print('that wasn\'t a palindrome')



# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
