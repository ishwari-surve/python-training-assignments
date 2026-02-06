#Display all files with given extension from a directory

import os
import sys

def FileSearch(DirName, Extension):
    try:
        for file in os.listdir(DirName):
            if file.endswith(Extension):
                print(file)
    except Exception:
        print("Error while accessing directory")

def main():
    if len(sys.argv) != 3:
        print("Invalid input")
        return

    DirName = sys.argv[1]
    Extension = sys.argv[2]

    if os.path.isdir(DirName):
        FileSearch(DirName, Extension)
    else:
        print("Directory not found")

if __name__ == "__main__":
    main()
