#Q1: Check File Exists in Current Directory
import os

def CheckFile(FileName):
    if os.path.exists(FileName):
        print("File exists in current directory.")
        return True
    else:
        print("File does not exist.")
        return False

def main():
    FileName = input("Enter file name: ")
    CheckFile(FileName)

if __name__ == "__main__":
    main()
