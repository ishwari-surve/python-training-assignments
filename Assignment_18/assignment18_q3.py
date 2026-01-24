#Accept N numbers and return minimum number

def MinimumOfList():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        value = int(input("Enter element: "))
        data.append(value)

    return min(data)


if __name__ == "__main__":
    result = MinimumOfList()
    print("Minimum element:", result)
