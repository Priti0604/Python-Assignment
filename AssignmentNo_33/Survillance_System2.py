import psutil
import sys
import os
import time
import schedule

from thread_monitor import ThreadCommand
from openfiles_monitor import OpenFilesCommand   # STEP 2 IMPORT

def CreateLog(FolderName):
    Border = "-" * 50

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    FileName = os.path.join(
        FolderName,
        "Marvellous_%s.log" % time.strftime("%Y-%m-%d_%H-%M-%S")
    )

    fobj = open(FileName, "w")
    fobj.write(Border + "\n")
    fobj.write("Marvellous Platform Surveillance System\n")
    fobj.write("Log created at :" + time.ctime() + "\n")
    fobj.write(Border + "\n")
    fobj.close()

    print("CPU usage :", psutil.cpu_percent())

def main():
    if len(sys.argv) == 2:

        if sys.argv[1] == "--threads":
            ThreadCommand()

        elif sys.argv[1] == "--openfiles":   # STEP 2 FLAG
            OpenFilesCommand()

        elif sys.argv[1] == "--h":
            print("--threads  : Thread Monitoring")
            print("--openfiles: Open Files Monitoring")

    elif len(sys.argv) == 3:
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Arguments")

if __name__ == "__main__":
    main()