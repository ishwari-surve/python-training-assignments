#Q2: Display File Contents

def DisplayFile(FileName):
    try:
        with open(FileName, "r") as f:
            data = f.read()
            print("File Contents:\n")
            print(data)
    except FileNotFoundError:
        print("File not found.")

def main():
    FileName = input("Enter file name: ")
    DisplayFile(FileName)

if __name__ == "__main__":
    main()