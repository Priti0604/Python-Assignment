#Command line input

import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):
    Border = "-"*50
    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
            return

    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("Log file gets created with name : ",FileName)

    fobj = open(FileName,"w")
    fobj.write(Border + "\n")
    fobj.write("------Marvellous Platform Surveillance System-------\n")
    fobj.write("Log created at :"+ time.ctime() + "\n")
    fobj.write(Border + "\n")

    fobj.write("\n"*15)
    
    fobj.write(Border + "\n") 
    fobj.write("----------End of Log File---------\n")        

    print("CPU usage :",psutil.cpu_percent()) 

def main():
    Border = "-"*50
    print(Border)
    print("------------------Marvellous Platform Surveillance System----------------")
    print(Border)


    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This script is used to :")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Sends email with the log")
            print("4 : Store information about proccess")
            print("5 : Store info about the CPU usage")
            print("6 : Store info about the RAM usage")
            print("7 : Store info about the Secondary Memory usage")


        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the automation script as")
            print("Script.py TimeInterval DirectoryName")
            print("TimeInterval :the time in minutes for periodic scheduling")
            print("DirectoryName : Name of the directory to crreate auto logs")
            

        else:
            print("Use the given flags as :")
            print("--u : used to display the usage")
            print("--h : used to display the help") 
 
     #Python DEmo.py % Marvellous
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval : ",sys.argv[1])
        print("Directory name :",sys.argv[2])
        
        #Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])


        print('Platform Surveillance System Started  Successfully')
        print("Directory created with name : ",sys.argv[2])
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