# calculator

n1 = float(input("Enter 1st no. = "))
n2 = float(input("Enter 2nd no. = "))
print("Enter for multiplication '*', addition '+', substraction '-', exponential '**', division '/'")
a = (input("Enter the operators = "))
if(a=='*'):
    print("n1*n2 = ",n1*n2)
elif(a=='+'):
    print("n1+n2 = ",n1+n2)
elif(a=='-'):
    print("n1-n2 = ",n1-n2)
elif(a=='**'):
    print("n1**n2 = ",n1**n2)
elif(a=='/'):
    print("n1/n2 = ",n1/n2)