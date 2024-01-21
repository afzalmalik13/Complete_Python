'''
Implement a program that asks the user to enter a password and keeps asking until the correct 
password is entered. Use a while loop for this.
'''

import time
pasw = 'Rengoku123@@'
attempt = 5
while 1:
    attempt -= 1
    user = str(input('Enter your password: '))
    if user == pasw:
        print('Correct Password')
        break
    if user != pasw:
        print('Incorrect Password \n\t Try again \n')
    if attempt == 0:
        print('Too many attempts \n\t Try after some time')  
        time.sleep(20)
    time.sleep(0.5)
    