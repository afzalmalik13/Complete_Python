'''
Write a program that calculates the factorial of a given positive integer using a while loop
'''

n = int(input('Enter the no. = '))
fact = 1
while n>0:
    fact *= n
    n -= 1
print(fact)