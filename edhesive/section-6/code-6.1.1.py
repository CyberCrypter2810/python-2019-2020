# section-6.1.1.py

c = 0
w = input("Please enter a word: ")
c = c + 1
print("#" + str(c) + ": You entered " + w + ".")

while (w != "STOP"):
    w = input("Please enter the next word: ")
    if (w != "STOP"):
        c = c + 1
        print("#" + str(c) + ": You entered " + w + ".")

print("All done. " + str(c) + " words entered.")
