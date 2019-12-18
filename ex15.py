from sys import argv
#import the function argv to help us read files
script, filename = argv
#in order to call it we need to feed it two arguments. the script
#name and the file we are trying to read.
txt = open(filename)
#open is a function that reads the file we pass through argv.
#We store this function in the variable txt
print(f"here's your file {filename}:")
print(txt.read())
close(txt)
#Prints a string with the name of the file we are reading included.
#Function used to read the actual file and print it.
print("Type the filename again:")
file_again = input("> ")
#Asking for another filename to open. creates a new variable file_again
###to store the new file given by the user.
txt_again = open(file_again)
#new variable to run the new file given.
print(txt_again.read())
close(txt_again)
#prints the new file passed. and ends the program.
