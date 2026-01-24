#Accept N numbers and return maximum number

def MaximumOfList():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        value = int(input("Enter element: "))
        data.append(value)

    return max(data)


if __name__ == "__main__":
    result = MaximumOfList()
    print("Maximum element:", result)
