# Python program to print all the even numbers within the given range.

num = int(input('Enter the number => '))
for i in range(1, num+1):
    if(i % 2 == 0):
        print(i)