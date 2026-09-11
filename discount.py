age=int(input("Enter your age "))
t=1000

if age<=12:
    print(" dicount applicable your ticket price is",t-(t/100)*10)
else:
    print('discount    is not applicable your ticket price is ',t)



