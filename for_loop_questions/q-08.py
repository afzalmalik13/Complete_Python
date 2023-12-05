# Python program to check if the given string is a palindrome.

str1 = input('Enter the string => ')
str2 = ''
for i in str1:
     str2 = i + str2
if (str1 == str2):
    print(f'{str1} \n \t Given string is a plaindrome.')
else:
    print(f'{str1} \n \t Given string is not a plaindrome.')