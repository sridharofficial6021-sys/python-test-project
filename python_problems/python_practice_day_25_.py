try:
    a=int(input())
    b=int(input())
    print(a+b)

except Exception:
    print("some thing") 


try:
    a=int(input())
    b=int(input())
    print(a+b)

except Exception as e:
    print("some thing", e)

finally:
    print("some thing")


    

try:
    a=int(input())
    b=int(input())
    c=int(input())

except ValueError as e:
    print("value as",e) 
except TypeError as e:
    print("type error",e)










