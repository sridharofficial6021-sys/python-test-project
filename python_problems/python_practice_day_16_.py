class laptop:
    def __init__(self):
        self.ram=""
        self.proc=""

    def display(self):
        print("ram:",self.ram) 
        print("proc:",self.proc)


hp=laptop()
dell=laptop()

hp.ram="8gb"
hp.proc="i5"

dell.ram="16gb"
dell.proc="i7"

hp.display()
dell.display()