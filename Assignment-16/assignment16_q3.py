#Add two numbers using function Add()

def Add(a, b):
    return a + b

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    result = Add(x, y)
    print("Addition is:", result)

if __name__ == "__main__":
    main()
