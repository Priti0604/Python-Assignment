#Arithmetic Class

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter Value1: "))
        self.Value2 = int(input("Enter Value2: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
            return "Division by zero not allowed"
        return self.Value1 / self.Value2

obj = Arithmetic()
obj.Accept()

print("Addition:", obj.Addition())
print("Subtraction:", obj.Subtraction())
print("Multiplication:", obj.Multiplication())
print("Division:", obj.Division())
