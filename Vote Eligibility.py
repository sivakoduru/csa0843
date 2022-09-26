try:
    age=int(input("enter age of the person:"))
    if (age>=18):
        print ("your allowed to vote")
    elif (age<18):
        result=18-age
        print("your allowed vote after years:",result)
except ValueError:
    print("in valid input ")
