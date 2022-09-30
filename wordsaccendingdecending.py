n=int(input("enter number of words : "))
words=[]
print("enter the words")
for i in range(0,n):
    y=str(input())
    words.append(n)
print("words=",words)
print("input your choice:")
choice=input("assending or dessending :")
if(choice == 'a'or choice == 'A'):
    words.sort()
    print("the ascending sorted list are : ",words)
elif(choice == 'd' or choice == 'D'):
    words.sort(reverse=True)
    print("the descending sorted list are = ",words)
else:
    print("invalid input")
