#Copy File Contents into Another File


source_file = input("Enter the source file name :")
destination_file = input("Enter the destination file name :")

try:
    source = open(source_file,"r")
    destination = open(destination_file,"w")
    data = source.read()
    destination.write(data)
    print("File contents copied successfully")
    source.close()
    destination.close()
except FileNotFoundError:
    print("Source file is not present in current directory")

    