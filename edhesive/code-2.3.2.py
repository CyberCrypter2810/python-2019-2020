#Section 2.3.2.py

'''
Enter the Feet for the first piece of fabric: 3
Enter the Inches for the first piece of fabric: 11

Enter the Feet for the second piece of fabric: 2
Enter the Inches for the second piece of fabric: 5
'''

feet1 = int(input("Enter the Feet for the First Piece of Fabric : "))
inches1 = int(input("Enter the Inches for the First Piece of fabric: "))

feet2 = int(input("Enter the Feet for the second piece of fabric: "))
inches2 = int(input("Enter the Inches for the Second Piece of Fabric: "))

totalinches = inches1 + inches2 + (feet1 *12) + (feet2 *12)
feetequation = int(totalinches / 12)
inchesremainder = int(totalinches % 12)

#print(str(feetequation) + "Feet " + str(inchesremainder) + "Inches") #I would prefer this in real life
print("Feet: " + str(feetequation) + " Inches: " + str(inchesremainder))
