#importing sys library to use argv function
import sys
#allows us to use argv (in the terminal) by calling the name of the
#script and the file argv is opening (in this case its input_encoding
# and error as well? or just only error is being opened?)
script, input_encoding, error = sys.argv

#creates a function that allows us to read the text file.
#if statement checks to see if there is something in the variable 'line'
#As readline iterates through each line, the if-statement closes it
#when there's an empty string in 'line'
#print_line embedded in this function to simplify the code. You can always
#reference it if you're unsure what it does.
#main is ran again inside the main function to make sure it loops
#the looping is once again halted by the if-statement. As long as it's not an
#empty string then it will keep running
def main(language_file, encoding, errors):
	line = language_file.readline()
	
	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)

#This function does the actual encoding and decoding of the languages file.
def print_line(line, encoding, errors):
	#returns a copy of the string with both leading and trailing characters stripped.
	#strip removes the \n on the 'line' string
	next_lang = line.strip()
	#takes in a string variable with \n filtered and converts the string
	#into bytes using the '.encode function'
	raw_bytes = next_lang.encode(encoding, errors = errors)
	#converts a byte variable into a string
	#errors are stored in the errors variable
	cooked_string = raw_bytes.decode(encoding, errors = errors)
	#then both bytes and strings are printed out, they should be equivalent.
	print(raw_bytes, "<===>", cooked_string)

#This opens the languages.txt file
languages = open("languages.txt", encoding = "utf-8")

#Runs the main function and starts the loop.
main(languages, input_encoding, error)