# Python program to check if a given number is an Armstrong number
num = (input('Enter the number => '))
arm = 0
for i in num:
    arm = arm + (int(i) ** len(num))
print(f'Number = {arm}')
if (num == arm):
    print('\tGiven number is an Armstrong number.')
else:
    print('\tGiven number is an Armstrong number.')