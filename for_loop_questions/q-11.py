# Python program to count the number of even and odd numbers from a series of numbers.

lst = [2, 4, 5, 7, 9, 1, 0, 67]
even = 0
odd = 0
for i in lst:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'Number of even numbers are {even}')
print(f'Number of odd numbers are {odd}')
