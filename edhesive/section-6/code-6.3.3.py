# Section 6.3.3.py

#python 3 for this to work
i = 0
for j in range(10,91):
    print(j, end=" ")
    i = i + 1
    if(i == 10):
        print("\n")
    if (i > 10):
        i = 1
