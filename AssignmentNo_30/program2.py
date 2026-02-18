#Count Words in a File


filename = input("Enter the file name :")

file = open(filename,"r")
data = file.read()
words = data.split()
print("Number of words in the file are :",len(words))
file.close()
