#Remove Duplicates + Execution Time



import os
import sys
import hashlib
import time

# Function to write messages into log file
def WriteLog(message):
    file = open("Log.txt", "a")
    file.write(message + "\n")
    file.close()

# Function to calculate checksum of file
def GetChecksum(path):
    file = open(path, "rb")
    data = file.read()
    file.close()
    return hashlib.md5(data).hexdigest()

# Function to remove duplicate files
def RemoveDuplicateFiles(directory):
    files_seen = {}

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            checksum = GetChecksum(filepath)

            if checksum in files_seen:
                os.remove(filepath)
                WriteLog(filename + " deleted (Duplicate)")
            else:
                files_seen[checksum] = filename

# Main function
def main():
    start_time = time.time()

    try:
        if len(sys.argv) != 2:
            WriteLog("Invalid arguments")
            return

        directory = sys.argv[1]

        if not os.path.isdir(directory):
            WriteLog("Directory does not exist")
            return

        RemoveDuplicateFiles(directory)

    except Exception as e:
        WriteLog(str(e))

    end_time = time.time()
    WriteLog("Execution Time: " + str(end_time - start_time))

# Entry point
main()
