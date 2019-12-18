from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit return.")

input("?")
#w for opening the file in write mode.
print("Opening the file...")
#w sets the open function to write mode. without w we cannot use the
#write function later on as there is no place to write anything in.
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
#I read on that blog that is not needed as using the open
#function with w instantly starts the truncating process because
#w lets you open the document in write mode.
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to a file.")
#using the format function to read in the new lines created. we use
#brackets to insert the new user inputs.
target.write('{}\n{}\n{}\n'.format(line1,line2,line3))

print("And finally, we close it.")
target.close()
