#Section 2.3.3.py

'''
Example 1:
Enter the hour: 8
Enter the minute: 15

Example 2:
Enter the hour: 9
Enter the minute: 46
'''

oldhour = int(input("Enter an hour: "))
oldminute = int(input("Enter the minute: "))

add = oldminute + 15 + (oldhour * 60)
newhour = int(add / 60)
newminute = int(add % 60)

if(newhour > 12):
	newhour = newhour - 12;


print("Hours: " + str(newhour) + "\nMinutes: " + str(newminute))
