x=int(input("x="))
n=int(input("n="))
print("1.Additon\n2.substration\n3.Multiplication\n4.Division\n5.power")
option=int(input("option:"))
if option==1:
    result=x+n
    print("sum =",result)
elif option==2:
    result=x-n
    print("sub=",result)
elif option==3:
    result=x*n
    print("mul=",result)
elif option==4:
    result=x/n
    print("div=",result)
elif option==5:
    result=x**n
    print("power=",result)
else:
    print("invalid input")
