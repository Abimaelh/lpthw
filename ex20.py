from sys import argv

#script name and the argument input_file
script, input_file = argv

#create a function print_all that takes in a variable has to be f for 'file' and prints it out by using the read method. Only need read
#because current_file opens the file.
def print_all(f):
	print(f.read())

#moves the location of the pointer
def rewind(f):
	f.seek(0)

#defines a function that takes in two arguments, line_count - stores the line number we're in, and f - the file. Then it prints the 
#line we're on of that file.
def print_a_line(line_count, f):
	print(line_count, f.readline())

#variable that we pass to all the other functions. it opens a file it is given.
current_file = open(input_file)

print("First let's print the whole file:\n")

#print_all is a function that takes in a file that is opened by the current_file variable and read by its function. the output is the information
#inside the file.
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

#rewind is a function that sets the pointer of the file to 0 (or where the first letter which is 'T' in test2.txt). 
#0 is where the pointer always starts, unless otherwise specified. 
rewind(current_file)

print("Let's print three lines:")

#prints out the number 1 along with the first line in the file
current_line = 1
print_a_line(current_line, current_file)

#adds a number to the current_line and prints out the second line in the text file.
current_line = 1
print_a_line(current_line, current_file)

#everytime we call this function it reads the next line after a line-break.
current_line = 1
print_a_line(current_line, current_file)

current_line = 1
print_a_line(current_line, current_file)

