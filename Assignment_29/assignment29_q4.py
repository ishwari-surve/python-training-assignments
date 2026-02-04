#Q4: Compare two files (Command Line)
import sys

def CompareData(Fname1, Fname2):

    file1 = open(Fname1, "r")
    file2 = open(Fname2, "r")

    text1 = file1.read()
    text2 = file2.read()

    file1.close()
    file2.close()

    if text1 == text2:
        print("Success")
    else:
        print("Failure")

def main():

    if len(sys.argv) < 3:
        print(" Provide two file names:")
        return

    CompareData(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
