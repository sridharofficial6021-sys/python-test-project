class phone():
    chargertype="type c"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def display(self):
        print("brand:",self.brand)
        print("price:",self.price) 
        print("type:", phone.chargertype)

        

samsumg=phone("samsung",10000) 
samsumg.display()


redmi=phone("redmi",15000)
redmi.display()