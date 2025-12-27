class animal():
    def sound(self):
        print("animal make sound")

class dog(animal):
    def sound(self):
        print("dog is hungry") 

class birds(dog):
    def sound(self):
        print("birds sings")

d1=birds()
d1.sound()                      



def add(a,b,c=0):
    print("sum=",a+b+c)

add(2,3)
add(2,3,4,)    