#Display File Contents

import os

filename = input(("Enter the file name :"))

try:
    file = open(filename,"r")
    data = file.read()
    print("File contents are :",data)
    file.close()
except FileNotFoundError:
    print("File is not present in current directory")    
  


