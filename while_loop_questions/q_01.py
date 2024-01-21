'''
Write a program that takes an integer input from the user and counts down from that number to 1 
using a while loop.
'''

import time

n = int(input('Enter the no. = '))
while n>0:
    print(n)
    time.sleep(2)
    n -= 1