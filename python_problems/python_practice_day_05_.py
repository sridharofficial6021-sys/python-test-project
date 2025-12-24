salary=int(input("enter the salary:"))
age=int(input("enter the age:"))
if(salary>=20000 or age<=25):
    loan=int(input("enter the loan:"))
    if(loan>50000):
        print("maximum loan is 50000")
    else:
        print("you are eligible for loan")
else:
    print("you are not eligible for loan")
    


a=int(input("enter a:"))    
b=int(input("enter b:"))
c=int(input("enter c:"))
d=int(input("enter d:"))
e=int(input("enter e:"))
f=(a+b+c+d+e)/5
if(f>35):
    print("good for more study")
else:
    print("you need addition class")