string = input("enter the string:")
rev = reversed(string)
if list(string) == list(rev):  
   print("THE STRING IS PALINDROME")  
else:  
   print("THE STRING IS NOT PALINDROME")
