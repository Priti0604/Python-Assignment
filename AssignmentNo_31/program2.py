#Rename Files (.txt → .doc)

import os
import sys

def WriteLog(msg):
    f = open("Log.txt", "a")
    f.write(msg + "\n")
    f.close()

def RenameFiles(directory, old_ext, new_ext):
    try:
        for file in os.listdir(directory):
            if file.endswith(old_ext):
                old = os.path.join(directory, file)
                new = os.path.join(directory, file.replace(old_ext, new_ext))
                os.rename(old, new)
                WriteLog(f"{file} renamed")

    except Exception as e:
        WriteLog(str(e))

RenameFiles(sys.argv[1], sys.argv[2], sys.argv[3])
