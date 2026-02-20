import sys
import time
import schedule
from logger_module import CreateLog

def fun(DirName):
    CreateLog(f"Backup triggered for directory : {DirName}")

def main():
    Border = "-" * 50
    print(Border)
    print("Marvellous Data Shield System")
    print(Border)

    if len(sys.argv) == 3:
        schedule.every(int(sys.argv[1])).minutes.do(fun, sys.argv[2])
        print("Logging system started")
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid arguments")

if __name__ == "__main__":
    main()