# match case statement

x = float(input("Enter the value of x = "))
match x: # x is the variable to match
    case 0: # if x is zero
        print("x is zero")
    case 10 if x / 5 == 2: # case with if condition
        print('This is special no.')
    case _ if x % 2 == 0: # empty case with if condition , this is like a complete if
        print('x is completely divisible by 2')
    case _: # default case(case _ = case other), if the above conditions are not execute then default case execute like else
        print('x is not divisible by 2')