#Vertical star pattern

def Pattern(n):
    for i in range(n):
        print("*")

def main():
    num = int(input("Enter number: "))
    Pattern(num)

if __name__ == "__main__":
    main()
