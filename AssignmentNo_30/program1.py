#Count Lines in a File

filename = input("Enter the file name :")

file = open(filename,"r")
lines = file.readlines()
print("Number of lines in the file are :",len(lines))   
file.close()

