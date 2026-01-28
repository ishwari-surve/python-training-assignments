class Circle:

    PI = 3.14  

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter radius of circle: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius


obj = Circle()

obj.Accept()
obj.CalculateArea()
obj.CalculateCircumference()

print("Area of circle:", obj.Area)
print("Circumference of circle:", obj.Circumference)
