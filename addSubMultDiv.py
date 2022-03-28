while True:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print("Enter your choice 1-5\n1. Addition\n2.Subtraction\n3.Division\n4.Multiplication\n5.Exit")
    n=int(input("enter your choice"))
    if n==1:
        print("Addition: ",a+b)
    elif n==2:
        print("Subtraction: ",a-b)
    elif n==3:
        print("Division: ",a/b)
    elif n==4:
        print("Multiplication: ", a / b)
    elif n==5:
        break;
    print("enter valid choice:")
