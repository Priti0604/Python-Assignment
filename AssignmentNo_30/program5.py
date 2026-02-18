#Search a Word in a File

filename = input("Enter the file name :")
word = input("Enter the word to search :")
file = open(filename,"r")
data = file.read()
if word in data:
    print("Word is present in the file")
else:
    print("Word is not present in the file")
file.close()

