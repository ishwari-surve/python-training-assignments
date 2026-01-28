class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors of", self.Value, "are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total = total + i
        return total

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        else:
            return False


def main():
    obj1 = Numbers()
    print("Is Prime:", obj1.ChkPrime())
    obj1.Factors()
    print("Is Perfect:", obj1.ChkPerfect())

    print()

    obj2 = Numbers()
    print("Is Prime:", obj2.ChkPrime())
    obj2.Factors()
    print("Is Perfect:", obj2.ChkPerfect())


if __name__ == "__main__":
    main()
