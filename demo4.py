m=int(input("enter a number :"))
print(f"{m} is {m//60} hours{m%60} minutes")

d=int(input("enter a number :"))
print(f"{d} : last digit is {d%10}")

#question 3
role=input("enter your role :")
age=int(input("enter your age :"))
a=role=="student" and age<21
print(f" Eligibal : {a}")
#soham pakhare