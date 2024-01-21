'''
 Write a program that checks if a given string is a palindrome (reads the same forwards and
backwards) using a while loop.
'''
str = (input('Enter the string = '))
pal = ''
i = 1
while len(str)>len(pal):
    new = str[-i]
    pal += new
    i += 1
if str == pal:
    print(f"{str} \n\t Given string is a palindrome")
else:
    print(f"{str} \n\t Given string is not a palindrome")