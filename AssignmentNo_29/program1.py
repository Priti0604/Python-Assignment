#Check File Exists in Current Directory

import os

filename = input("Enter the file name :")

if os.path.isfile(filename):
    print("File is present in current directory")
else:    
    print("File is not present in current directory")