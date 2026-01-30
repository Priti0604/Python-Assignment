#BankAccount Class


class BankAccount:
    ROI = 10.5   # Class variable

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print("Name:", self.Name)
        print("Balance:", self.Amount)

    def Deposit(self):
        amt = float(input("Enter amount to deposit: "))
        self.Amount += amt

    def Withdraw(self):
        amt = float(input("Enter amount to withdraw: "))
        if amt <= self.Amount:
            self.Amount -= amt
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


# Creating object
acc = BankAccount("Amit", 5000)

acc.Display()
acc.Deposit()
acc.Withdraw()
acc.Display()

print("Interest:", acc.CalculateInterest())
