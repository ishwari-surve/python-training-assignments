#Display length of name

def NameLength(name):
    return len(name)

def main():
    name = input("Enter name: ")
    length = NameLength(name)
    print("Length of name is:", length)

if __name__ == "__main__":
    main()
