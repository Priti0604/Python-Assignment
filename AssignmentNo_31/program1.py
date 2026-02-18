#Display Files with Given Extension


import os
import sys

def WriteLog(msg):
    f = open("Log.txt", "a")
    f.write(msg + "\n")
    f.close()

def SearchFiles(directory, extension):
    try:
        if not os.path.isdir(directory):
            WriteLog("Directory not found")
            return

        for file in os.listdir(directory):
            if file.endswith(extension):
                WriteLog(file)

    except Exception as e:
        WriteLog(str(e))

SearchFiles(sys.argv[1], sys.argv[2])
