a=int(input("enter first number : "))
b=int(input("enter second number : "))
c=int(input("enter 1 for addition 2 for sub 3.for mult 4 for div "))

match c :
    case 1:
        print("addition is =",a+b)
    case 2:
        print("sub is = ",a-b)
    case 3:
        print("multi is = ",a*b)
    case 4:
        print("div is = ",a/b)
    case _:
        print("enter valid choic")