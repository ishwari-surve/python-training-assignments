class BankAccount:
    ROI = 10.5   
  
    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print("Account Holder:", self.Name)
        print("Current Balance:", self.Amount)

    def Deposit(self):
        dep = float(input("Enter amount to deposit: "))
        self.Amount = self.Amount + dep
        print("Amount deposited successfully.")

    def Withdraw(self):
        wd = float(input("Enter amount to withdraw: "))
        if wd <= self.Amount:
            self.Amount = self.Amount - wd
            print("Withdrawal successful.")
        else:
            print("Insufficient balance. Withdrawal not allowed.")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


def main():
    acc1 = BankAccount("Ishwari", 5000)
    acc1.Display()
    acc1.Deposit()
    acc1.Withdraw()
    print("Interest:", acc1.CalculateInterest())

    print()

    acc2 = BankAccount("Radha", 10000)
    acc2.Display()
    acc2.Deposit()
    acc2.Withdraw()
    print("Interest:", acc2.CalculateInterest())


if __name__ == "__main__":
    main()
