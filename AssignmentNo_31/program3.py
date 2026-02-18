#Copy All Files from One Directory to Another


import os
import sys
import shutil

def WriteLog(msg):
    f = open("Log.txt", "a")
    f.write(msg + "\n")
    f.close()

def CopyFiles(src, dest):
    try:
        if not os.path.exists(dest):
            os.mkdir(dest)

        for file in os.listdir(src):
            shutil.copy(os.path.join(src, file), dest)
            WriteLog(file + " copied")

    except Exception as e:
        WriteLog(str(e))

CopyFiles(sys.argv[1], sys.argv[2])
