class student:
    def __init__(self):
        self.name=""
        self.reg=""

    def display(self):
        print("name",self.name ) 
        print("reg",self.reg ) 

s1=student()
s2=student()

s1.name="sri"
s2.name="guna"

s1.reg=21
s2.reg=22

s1.display()
s2.display()



class fruit:
    def __init__(self,col):
        self.color=col
apple=fruit("red")
print(apple.color)


class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.reg=reg
    def display(self):
        print("name",self.name) 
        print("reg",self.reg) 


t1=teacher("sri",1) 
t2=teacher("guna",2)
t1.display()
t2.display()         



class Calculator:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def add(self):
        print("add:", self.num1 + self.num2)

obj1 = Calculator(10, 20)
obj1.add()



