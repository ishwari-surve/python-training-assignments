class Demo:

    Value = 100   

    def __init__(self, a, b):
        self.no1 = a
        self.no2 = b

    def Fun(self):
        print("Calling Fun method")
        print("no1:", self.no1)
        print("no2:", self.no2)

    def Gun(self):
        print("Calling Gun method")
        print("no1:", self.no1)
        print("no2:", self.no2)


# main execution
obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()
