#Frequency of a String in File

import os
filename = input("Enter the file name :")
try:
    file = open(filename,"r")
    data = file.read()
    word = input("Enter the word to find frequency :")
    frequency = data.count(word)
    print("Frequency of the word is :",frequency)
    file.close()
except FileNotFoundError:
    print("File is not present in current directory")   

    
