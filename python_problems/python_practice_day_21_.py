class a():
    def __init__(self):
        print("a")

    def display(self):
        print("you are class a")

class b():
    def __init__(self):
        super ().__init__()
        print("b")

class c(b,a):
    def __init__(self):
        super ().__init__()
        print("c")
    def display():
        print("you are class c")

obj1=c()        
                               