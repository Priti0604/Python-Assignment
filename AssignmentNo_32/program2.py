#Find Duplicate Files (Log Only)

import os
import sys
import hashlib

def WriteLog(msg):
    f = open("Log.txt", "a")
    f.write(msg + "\n")
    f.close()

def FindDuplicates(directory):
    seen = {}
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        f = open(path, "rb")
        hash = hashlib.md5(f.read()).hexdigest()
        f.close()

        if hash in seen:
            WriteLog(file)
        else:
            seen[hash] = file

FindDuplicates(sys.argv[1])
