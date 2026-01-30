#Numbers Class


class Numbers:
    def __init__(self):
        self.Value = int(input("Enter number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors:", end=" ")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

    def ChkPerfect(self):
        return self.SumFactors() == self.Value


# Creating object
num = Numbers()

print("Prime:", num.ChkPrime())
print("Perfect:", num.ChkPerfect())
num.Factors()

