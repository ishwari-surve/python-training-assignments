#Sum of factors

def SumFactors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def main():
    num = int(input("Enter number: "))
    print("Sum of factors:", SumFactors(num))

if __name__ == "__main__":
    main()
