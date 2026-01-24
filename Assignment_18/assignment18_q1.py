#Accept N numbers from user, store in list, return addition of all elements

def AdditionOfList():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        value = int(input("Enter element: "))
        data.append(value)

    total = sum(data)
    return total


if __name__ == "__main__":
    result = AdditionOfList()
    print("Addition of elements:", result)
