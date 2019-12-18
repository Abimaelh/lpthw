cars = 100 #assigns the variable 'cars' an integer value of 100
space_in_car = 4 #assigns the variable 'space_in_car' an floating value of 4.0
drivers = 30 #assigns the variable 'drivers' an integer value of 30
passengers = 90 #assigns the variable 'passengers' an integer value of 90
cars_not_driven = cars - drivers #assigns a variable 'cars_not_driven' the
#value of 'cars' which equals 100 MINUS the value of 'drivers' which equals
#30. So basically 'cars_not_driven' = 100-30 which comes out to 70.
cars_driven = drivers #'cars_driven' is equal to the value of 'drivers' which is
#30. This variable will be used in another variable. so it was renamed just to
#make it easier to work with.
carpool_capacity = cars_driven * space_in_car #'cars_driven' = 30 MULTIPLIED
#by 'space_in_car' = 4.0 will give us a 'carpool_capacity' of 120.0
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
