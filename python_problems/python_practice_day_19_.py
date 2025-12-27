class laptop():
    chargertype="type c"

    def __init__(self):
        self.brand=""
        self.price=1000

    def setprice(self,price):
        self.price=price 


    def getprice(self):
        print(self.price)


    @ classmethod
    def changechargertype(cls):
        cls.chargertype="type b" 

    @ staticmethod
    def into():
        print("this is laptop class") 


hp=laptop()
hp.setprice(20000) 
hp.getprice()
laptop.changechargertype()
hp.into()



