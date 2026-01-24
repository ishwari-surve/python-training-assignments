#Factorial of a number

def Factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def main():
    num = int(input("Enter number: "))
    print("Factorial:", Factorial(num))

if __name__ == "__main__":
    main()
