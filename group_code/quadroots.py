#quadroots.py gbpm

'''
Quadtratic calulator
D is the Discriminant of the quadratic equation. D = b^2 - 4ac
'''

def roots(a,b,c):
	D = (b*b - 4*a*c)
	print()
	print("D = " + str(D))
	if (D >=0): #This is a check for a positive D
		print("REAL ROOTS")
		D = D**0.5 #Calculating the square root of D
		x1 = (-b + D) / (2*a)
		x2 = (-b - D) / (2*a)
		print("x1 = " + str(x1) + "\nx2 = " + str(x2))
		
	elif(D > 0): #This is a check for a negative D
		print("REAL ROOTS")
		D = (D * -1)**0.5; #Changes the negative into a positive
		#Then takes the square root of D then represent it with an "i"
		print("IMAGINARY ROOTS")
		print("x1 = -" + str(b/2*a) + " - " + str(D/2*a) + "i")
		print("x1 = -" + str(b/2*a) + " + " + str(D/2*a) + "i")
		
if __name__ == '__main__':
	print("Input a,b,and c for the quadratic (ax^2 + bs + c)")
	a = input("Enter a: ")
	b = input("Enter b: ")
	c = input("Enter c: ")
	roots(float(a), float(b), float(c))
