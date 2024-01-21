'''
Write a Python program to construct the following pattern, using a nested for loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

n = 5
for i in range(n):
    print('* '*(i+1))
for i in range(1,n):
    print('* '*(n-i))