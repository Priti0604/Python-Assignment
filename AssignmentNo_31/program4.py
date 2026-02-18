#Copy Files with Specific Extension

import os
import sys
import shutil

def WriteLog(msg):
    f = open("Log.txt", "a")
    f.write(msg + "\n")
    f.close()

def CopyByExtension(src, dest, ext):
    try:
        if not os.path.exists(dest):
            os.mkdir(dest)

        for file in os.listdir(src):
            if file.endswith(ext):
                shutil.copy(os.path.join(src, file), dest)
                WriteLog(file + " copied")

    except Exception as e:
        WriteLog(str(e))

CopyByExtension(sys.argv[1], sys.argv[2], sys.argv[3])
