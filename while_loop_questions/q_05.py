'''
Write a program that generates and prints the first n terms of the Fibonacci sequence using a while 
loop.
'''
n = int(input('Enter the no. = '))
pre = 0
next = 1
while n>1:
    pre_pre = pre
    pre = next
    next = pre_pre + pre
    n -= 1
    print(next,end = ' ')
print("\n\t The above sequence of series is fabonacci Series") 

