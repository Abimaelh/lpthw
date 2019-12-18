#import argv command from library sys
from sys import argv
#setting up the arguments argv needs to run. Always takes in 1 at least
#the first one is always the name of script itself.
#second, is the name of the file you are trying to read
script, filename = argv
#assign a variable to open the file we are trying to read.
#we must open it first before we can read it.
thefile = open(filename)
print(f"I'm going to print out {filename}:")
#now that the file is open we can use the read function to read it.
print(thefile.read())

#I guess i didn't learn it very well the first time.
#struggled with this part that is basically the last example.
