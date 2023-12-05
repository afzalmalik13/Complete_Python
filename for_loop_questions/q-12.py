# Python program to check the prime numbers.

num = int(input('Enter the number => '))
count = 0
for i in range(1,num+1):
    if num % i == 0:
        count += 1

if count == 2:
    print('Given no. is a prime no.')
else:
    print('Given no. is not a prime no.')