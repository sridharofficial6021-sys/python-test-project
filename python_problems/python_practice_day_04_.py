mark=int(input())
if(mark>35):
    print("pass")
else:
    print("fail")

income=int(input())    
if(income>7000):
    print("scholarship is not avalible")
else:
    print("scholarship is avalible")


a=int(input())
if(a%2==0):
    print("even")
else:
    print("odd")


score=int(input())
if(score<35):
    print("poor student")

elif(score>35 and score<70):
    print("avarage student")
elif(score>70 and score<100):
    print("good student")

else:
    print("invalid score")


a=int(input())    
b=int(input())
operation=input("add/sub/mul/div")
if(operation=="add"):
    print(a+b)

elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a%b)
else:
    print("invalid operation")



score=int(input())
if(score>70):
    name=input("enter the name:")
    age=input("enter the age:")
    departmant=input("enter the departmant:")

    print("your are eligible")

else:
    print("your are not eligible")