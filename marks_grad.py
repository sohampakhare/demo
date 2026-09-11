m=int(input("enter your marks : "))
if m>=0 and m<=100:
    if m>90:
        print("O grade ")
    elif m>80:
        print("A grade")
    elif m>65:
        print("B grade") 
    elif m<35:
        print("fail")
else:
    print("enter vaild marks")   
