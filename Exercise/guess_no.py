from random import *

c_num = randrange(1,101)
Attempt1 = 5
Attempt2 = 5
while 1:
    u1_num = int(input('Guess the Number by 1ST User: '))
    
    if u1_num == c_num:
        print(' Congrats User 1 Win with Attempt',Attempt1)
        break
    elif u1_num > c_num:
        print('Too Large And You Have',Attempt1, 'Attempt Left')
    else:
        print('Too Small And You Have',Attempt1, 'Attempt Left')
    if Attempt1<=0:
        break
    Attempt1-=1
    
    
    u2_num = int(input('Guess the Number by 2nd User: '))
    if u2_num == c_num:
        print(' Congrats User 2 Win with Attempt',Attempt2)
        break
    elif u2_num > c_num:
        print('Too Large And You Have',Attempt2, 'Attempt Left')
    else:
        print('Too Small And You Have',Attempt2, 'Attempt Left')
    if Attempt2<=0:
        break
    Attempt2-=1
if Attempt1==Attempt2==0:
    print('You Both Loose')