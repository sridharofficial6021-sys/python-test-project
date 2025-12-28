class shape():
    def area(self):
        return 0
    
class rectangle(shape):
    def area(self):
        l=10
        b=20

        print(l*b)

b1=rectangle()
b1.area()        


class person():
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,grade):
        super ().__init__(name)
        self.grade=grade

    def display(self):
        print("name:",self.name)
        print("grade:",self.grade)




s1=student("sri",1)
s1.display()   



class vehicle():
    def start(self):
        print("vehicle is start")


class car(vehicle):
    def start(self):
        print("car is start")

s1=car()
s1.start()  



class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class manager(employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print("name:", self.name)
        print("salary:", self.salary)
        print("department:", self.department)


m1 = manager("sri", 50000, "ece")
m1.display()

        





