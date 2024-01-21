'''
Write a program that checks if a given number is prime or not using a while loop
'''


n = int(input('Enter the no. = '))
count = 0
i = 1
while n>=i:
    if n%i == 0:
        count += 1
    i += 1
if count == 2:
    print('Given no. is a prime no.')
else:
    print('Given no. is not a prime no.')
