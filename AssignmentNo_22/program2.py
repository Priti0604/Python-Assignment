#Circle Class

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter Radius: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius:", self.Radius)
        print("Area:", self.Area)
        print("Circumference:", self.Circumference)

c1 = Circle()
c1.Accept()
c1.CalculateArea()
c1.CalculateCircumference()
c1.Display()
