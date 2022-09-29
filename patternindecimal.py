n=float(input("ENTER THE NUMBER :"))
r=int(input("ENTER THE NUMBER OF ROWS >>"))
for i in range(1,r+1):
    for j in range(1,i+1):
        print("%.1f"%n,end=" ")
        n=n+0.1
    print("\n")
