import sys
import time
import schedule
from logger_module import CreateLog
from email_module import SendEmail
from backup_module import BackupUpdatedFiles
from archive_module import CreateArchive

def fun(DirName):
    BackupUpdatedFiles(DirName, "Backup")
    CreateArchive("Backup")
    CreateLog("Backup archive created")
    SendEmail()

def main():
    if len(sys.argv) == 3:
        schedule.every(int(sys.argv[1])).minutes.do(fun, sys.argv[2])
        print("Data Shield System fully started")
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid arguments")

if __name__ == "__main__":
    main()