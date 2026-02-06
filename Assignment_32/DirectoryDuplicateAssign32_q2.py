#Q2: Find Duplicate Files in a Directory


import os
import sys
import hashlib

def GetChecksum(FilePath):
    fobj = open(FilePath, "rb")
    data = fobj.read()
    fobj.close()
    return hashlib.md5(data).hexdigest()

def FindDuplicateFiles(DirName):
    log = open("Log.txt", "w")
    checksum_dict = {}

    for file in os.listdir(DirName):
        path = os.path.join(DirName, file)

        if os.path.isfile(path):
            checksum = GetChecksum(path)

            if checksum in checksum_dict:
                log.write("Duplicate file found: " + file + "\n")
            else:
                checksum_dict[checksum] = file

    log.close()

def main():
    if len(sys.argv) != 2:
        return

    DirName = sys.argv[1]

    if os.path.isdir(DirName):
        FindDuplicateFiles(DirName)

if __name__ == "__main__":
    main()

