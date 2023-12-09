# Python program to print fabonicci series.

n = int(input("Enter the number => "))
preNum = 0
currNum = 1
for i in range(1, n+1):
    prepreNum = preNum
    preNum = currNum
    currNum = prepreNum + preNum
    print(currNum, end=" ")

