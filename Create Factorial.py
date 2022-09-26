a=int(input("enter the number: "))
fact=1
if a<0:
    for i in range(a,0):
        fact=fact*i
else:
    for i in range(1,a+1):
        fact=fact*i
print(fact)
