import sys
import time
import schedule
from logger_module import CreateLog
from email_module import SendEmail

def fun(DirName):
    CreateLog(f"Backup started for {DirName}")
    SendEmail()

def main():
    if len(sys.argv) == 3:
        schedule.every(int(sys.argv[1])).minutes.do(fun, sys.argv[2])
        print("Logging + Email notification started")
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid arguments")

if __name__ == "__main__":
    main()