a=int(input("enter no of fresh loaves:"))
b=int(input("enter no of old loaves:"))
c=a*185
d=b*185*0.6
e_float=c+d
print("regular price:185.00")
print("amount of fresh loaves:",c)
print("amount of old loaves:",d)
formatted_float = "{:.2f}".format(e_float)
print("total amount :",formatted_float)
