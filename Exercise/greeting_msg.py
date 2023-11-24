# greeting message

import time

tm = time.strftime('%H:%M:%S')
print(tm)
if('00:00:00'<tm<'12:00:00'):
    print("Good Morning Sir")
elif('12:00:00'<tm<'17:00:00'):
    print("Good  Afternoon Sir")
else:
    print("Good Evening Sir")

