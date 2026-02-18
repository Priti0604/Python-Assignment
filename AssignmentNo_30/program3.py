#Display File Line by Line


filename = input("Enter the file name :")
file = open(filename,"r")
lines = file.readlines()
for line in lines:
    print(line,end="")
file.close()
