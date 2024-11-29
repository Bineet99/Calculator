import math
print("______________________________WELCOME TO CALCULATOR_________________________________\n")
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")
print("Press 5 for Exponential")
print("Press 6 for Factorial")
print("Press 7 for Logarithm")
print("Press 8 for Square root")
print("Press 9 for Cube root")
print("Press 10 for Exit\n")
while True:
    
    ch=int(input("Enter your choice:"))
    
    if ch==1:
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number:"))
        result=(num1+num2)
        print(result)

    elif ch==2:
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number:"))
        result=(num1-num2)
        print(result)

    elif ch==3:
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number:"))
        result=(num1*num2)
        print(result)

    elif ch==4:
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number:"))
        result=(num1/num2)
        print(result)

    elif ch==5:
        num1=float(input("Enter the number:"))
        num2=float(input("Enter the power for that number:"))
        result=(num1**num2)
        print(result)

    elif ch==6:
        num = int(input("Enter a number: "))
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print(factorial)

    elif ch==7:
        num1 = float(input("Enter the number: "))
        base = float(input("Enter the base: "))
        if num1 <= 0:
            print("Error: Logarithm is undefined for non-positive numbers.")
        else:
            log_result = math.log(num1, base)
            print(log_result)

    elif ch==8:
        num = float(input("Enter a number: "))
        if num < 0:
            print("Square root is not defined for negative numbers.")
        else:
            result = math.sqrt(num)
            print(result)

    elif ch==9:
        num = float(input("Enter a number: "))
        cube_root = (num**(1/3))
        print(round( cube_root))

    elif ch==10:
        print("THANKS FOR USING CALCULATOR..")
        break

    else:
        print("INVALID CHOICE")
        
                  












        
        
        
        
