# Section 3.3.2.py

r = int(input("Enter the red: "))
g = int(input("Enter the green: "))
b = int(input("Enter the blue: "))

if (r < 0 or r > 255):
    print("Red color is not correct.")

if (g < 0 or g > 255):
    print("Green color is not correct.")

if (b < 0 or b > 255):
    print("Blue color is not correct.")
