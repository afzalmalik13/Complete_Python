'''
Create a program that takes an integer as input and prints the multiplication table for that number 
from 1 to 10 using a while loop
'''
n = int(input('Enter the no. = '))
i = 1
while i<=10:
    print(f"{n} X {i} = {n*i}")
    i += 1