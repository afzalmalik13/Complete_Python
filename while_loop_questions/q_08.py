'''
Implement a program that calculates the sum of the digits of a given integer using a while loop.
'''

n = int(input('Enter the no. = '))
sum = 0
while n>=1:
    sum += n
    n -= 1
print(sum)