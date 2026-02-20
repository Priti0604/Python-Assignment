# Command line input

import psutil
import sys
import os
import time
import schedule

from thread_monitor import ThreadCommand
from openfiles_monitor import OpenFilesCommand
from memory_monitor import MemoryCommand
from email_report import EmailCommand   # STEP 4 IMPORT

def CreateLog(FolderName):
    Border = "-" * 50

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, "Marvellous_%s.log" % timestamp)

    fobj = open(FileName, "w")
    fobj.write(Border + "\n")
    fobj.write("------Marvellous Platform Surveillance System-------\n")
    fobj.write("Log created at : " + time.ctime() + "\n")
    fobj.write(Border + "\n")
    fobj.write("CPU Usage : " + str(psutil.cpu_percent()) + "\n")
    fobj.write(Border + "\n")
    fobj.write("----------End of Log File---------\n")
    fobj.close()

    return FileName   # IMPORTANT for email

def main():
    Border = "-" * 50
    print(Border)
    print("Marvellous Platform Surveillance System")
    print(Border)

    if len(sys.argv) == 2:

        if sys.argv[1] == "--h":
            print("--threads    : Thread Monitoring")
            print("--openfiles  : Open Files Monitoring")
            print("--memory     : Memory Monitoring")
            print("--email      : Send Email Report")

        elif sys.argv[1] == "--threads":
            ThreadCommand()

        elif sys.argv[1] == "--openfiles":
            OpenFilesCommand()

        elif sys.argv[1] == "--memory":
            MemoryCommand()

        elif sys.argv[1] == "--email":
            logfile = CreateLog("MarvellousLogs")
            EmailCommand(logfile)

        else:
            print("Invalid option")

    elif len(sys.argv) == 3:
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print("Platform Surveillance System Started")
        print("Directory :", sys.argv[2])
        print("Interval :", sys.argv[1], "minutes")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")

    print(Border)
    print("Thank you for using Marvellous Automation")
    print(Border)

if __name__ == "__main__":
    main()