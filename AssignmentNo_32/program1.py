#Display Checksum of All Files


import os
import sys
import hashlib

def WriteLog(msg):
    f = open("Log.txt", "a")
    f.write(msg + "\n")
    f.close()

def Checksum(directory):
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            f = open(path, "rb")
            data = f.read()
            f.close()
            hash = hashlib.md5(data).hexdigest()
            WriteLog(file + " : " + hash)

Checksum(sys.argv[1])
