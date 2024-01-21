''' 
Write a program that calculates the sum of all even numbers from 1 to n, where n is an integer 
input by the user, using a while loop
'''
n = int(input('Enter the no. = '))
even = 0
while n>0:
    if n%2 == 0:
        even += n
    n -= 1
print(even)