#Q1: Count Lines in a File

def CountLines(FileName):

    fobj = open(FileName, "r")
    lines = fobj.readlines()
    fobj.close()

    return len(lines)

def main():

    FileName = input("Enter file name: ")

    result = CountLines(FileName)
    print("Total number of lines:", result)

if __name__ == "__main__":
    main()
