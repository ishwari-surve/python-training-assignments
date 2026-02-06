#Q3: Copy all files from one directory to another

import os
import sys
import shutil

def CopyFiles(SrcDir, DestDir):
    try:
        os.mkdir(DestDir)

        for file in os.listdir(SrcDir):
            SrcPath = os.path.join(SrcDir, file)
            DestPath = os.path.join(DestDir, file)

            if os.path.isfile(SrcPath):
                shutil.copy(SrcPath, DestPath)

    except Exception:
        pass

def main():
    SrcDir = sys.argv[1]
    DestDir = sys.argv[2]

    if os.path.isdir(SrcDir):
        CopyFiles(SrcDir, DestDir)
    else:
        pass

if __name__ == "__main__":
    main()
