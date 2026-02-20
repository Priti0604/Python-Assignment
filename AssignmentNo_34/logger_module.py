import time

def CreateLog(message):
    with open("DataShield.log", "a") as f:
        f.write(time.ctime() + " : " + message + "\n")