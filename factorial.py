def fact(n):

    if n==0:
        return 1

    return n*fact(n-1)

print("factorial is = ",fact(5))

square=lambda n:n*n
print(square(5))

add=lambda a,b:a+b

print("add is=",add(10,20))
