i = 0
numbers = [] #this is our list holding the values in i

while i < 6:
	print(f"At the top i is {i}")
	numbers.append(i)

	i = i + 1
	print("Numbers wow: ", numbers) #prints whats in the list 'numbers'
	print(f"At the bottom i is {i}") #the new updated number which is 1 since we append 1 each time


print("The numbers: ")

#prints out all the numbers in num
for num in numbers:
	print(num)