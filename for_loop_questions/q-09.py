# Python program that accepts a word from the user and reverses it.

w = input('Enter the word => ')
reverse = ''
for i in w:
    reverse = i + reverse
print(reverse)