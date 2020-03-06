# Section 4.2.2.py
# code somehow didn't accept, but completes requirements

x = 0
y = 0

while (x < 100):
	i = float(input("Input a Number to the sum: " + str(x) + "+"))
	x = x + i
	print(x)
	y = y + 1

print("Total Sum is: " + str(x))
print("Total of Numbers Inputed is: " + str(y))
