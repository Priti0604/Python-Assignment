#Compare Two Files (Command Line)

import sys                 #used yo access command line arguments   

file1 = (sys.argv[1],"r")
file2 = (sys.argv[2],"r")

f1 = open(file1)
f2 = open(file2)

data1 = f1.read()
data2 = f2.read()
if data1 == data2:
    print("Both files are same")
else:
    print("Both files are different")

f1.close()
f2.close()
