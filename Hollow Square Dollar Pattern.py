side=int(input("enter any side of a square:"))
ch=input("enter any character :")

print("hollow square dollar pattern")
for i in range(side):
    for j in range(side):
        if (i==0 or i==side-1 or j==0 or j==side-1):
            print('%c'%ch,end=' ')
        else:
            print(' ',end=' ')
    print()
