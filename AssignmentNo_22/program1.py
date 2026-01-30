#Demo Class

class Demo:
    Value = 0

    def __init__(self, a, b):
        self.no1 = a
        self.no2 = b

    def Fun(self):
        print("Fun Method:", self.no1, self.no2)

    def Gun(self):
        print("Gun Method:", self.no1, self.no2)

Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
