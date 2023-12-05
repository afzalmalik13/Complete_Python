# Python program that accepts a string and calculates the number of digits and letters.

str = input('Enter the string => ')
d = ''
l = ''
for i in str:
    if (i.isdigit()):
        d = d + i
    else:
        l = l + i
print(f'Number of digits are {len(d)}')
print(f'Number of letters are {len(l)}')