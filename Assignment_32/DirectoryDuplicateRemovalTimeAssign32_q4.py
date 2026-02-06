#Q4: Delete Duplicate Files + Log + Execution Time

import os
import sys
import hashlib
import time

def GetChecksum(FilePath):
    fobj = open(FilePath, "rb")
    data = fobj.read()
    fobj.close()
    return hashlib.md5(data).hexdigest()

def RemoveDuplicateFiles(DirName):
    log = open("Log.txt", "w")
    checksum_dict = {}

    start_time = time.time()

    for file in os.listdir(DirName):
        path = os.path.join(DirName, file)

        if os.path.isfile(path):
            checksum = GetChecksum(path)

            if checksum in checksum_dict:
                os.remove(path)
                log.write("Deleted duplicate file: " + file + "\n")
            else:
                checksum_dict[checksum] = file

    end_time = time.time()
    execution_time = end_time - start_time

    log.write("Execution Time: " + str(execution_time) + " seconds\n")
    log.close()

def main():
    if len(sys.argv) != 2:
        return

    DirName = sys.argv[1]

    if os.path.isdir(DirName):
        RemoveDuplicateFiles(DirName)

if __name__ == "__main__":
    main()
