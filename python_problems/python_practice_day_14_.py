s_username="sri"
s_password="123"

uname=input("enter value for username")
password=input("enter value for possword")

def validate():
    if(s_username==uname and s_password==password):
        return True
    else:
        return False
    
a=validate()    
print(a)




def add(r1, r2):
    return r1 + r2

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

added = add(a, b)
output = added * c

print(output)
