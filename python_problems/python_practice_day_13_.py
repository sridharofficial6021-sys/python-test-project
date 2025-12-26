def findevenodd(b):
    if b % 2 == 0:
        print("even")
    else:
        print("odd")

a = int(input("Enter a number: "))
findevenodd(a)



def passorfail(mark):
    if(mark>=35):
        print("pass")

    else:
        print("fail")
a=int(input("enter the mark:"))
passorfail(a)


def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)
a=int(input("enter the a:"))
b=int(input("enter the b:"))

printrange(a,b)