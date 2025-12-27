class dad():
    def phone(self):
        print("dad phone use")

class mom():
    def happy(self):
        print(" so happy for mom")

class son(dad,mom):
    def laptop(self):
        print("use to laptop")

sri=son()
sri.phone()
sri.happy() 




class grandpa():
    def phone(self):
        print("use grandpa phone")

class dad(grandpa):
    def money(self):
        print("dad money")

class son(dad):
    def laptop(self):
        print("use laptop")


sri=son()
sri.laptop()
sri.money()

d1=dad()
d1.phone()