#Copy File Contents into a New File (Command Line)

import sys                 #used yo access command line arguments

source_file = sys.argv[1]
destination_file = "Demo.txt"
file1 = open(source_file,"r")
content = file1.read()
file1.close()

file2 = open(destination_file,"w")
file2.write(content)
file2.close()
print("File copy successfully completed")
