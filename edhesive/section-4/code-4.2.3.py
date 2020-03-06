# Section 4.2.3.py

print("Type rock to end")
n = input("What pet do you have? ")
x = 0

while (n != "rock"):
	x = x + 1
	print("You have a " + n + " with a total of " + str(x) + " pet(s).")
	n = input("What pet do you have? ")
	
print ("You have " + str(x) + " pet(s)")
