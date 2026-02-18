#Remove Duplicate Files

import os
import sys
import hashlib

def WriteLog(msg):
    f = open("Log.txt", "a")
    f.write(msg + "\n")
    f.close()

def RemoveDuplicates(directory):
    seen = {}
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        f = open(path, "rb")
        hash = hashlib.md5(f.read()).hexdigest()
        f.close()

        if hash in seen:
            os.remove(path)
            WriteLog(file + " deleted")
        else:
            seen[hash] = file

RemoveDuplicates(sys.argv[1])
