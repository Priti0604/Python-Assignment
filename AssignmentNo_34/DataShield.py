#Command line input

import psutil
import sys
import os
import time
import schedule

def fun(DirName):
    pass


def main():
 
    Border = "-"*50
    print(Border)
    print("----------------------Marvellous Data Shield System----------------")
    print(Border)


    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This script is used to :")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of the backup periodically")
          
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the automation script as")
            print("Script.py TimeInterval Source Directory")
            print("TimeInterval :the time in minutes for periodic scheduling")
            print("Soruce Directory : Name of Directory to backup")
        else:
            print("Use the given flags as :")
            print("--u : used to display the usage")
            print("--h : used to display the help") 
 
     #Python DEmo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval : ",sys.argv[1])
        print("Directory name :",sys.argv[2])
        
        #Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(fun,sys.argv[2])


        print('Data Shield  System Started  Successfully')
        print("Time interval in minutes : ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")

        #Wait till abort
        while True :
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--u : used to display the usage")
        print("--h : used to display the help")

    print(Border)
    print("----Thank You for using our script------------")
    print(Border)


if __name__ == "__main__":
    main()      