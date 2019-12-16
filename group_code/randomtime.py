# randomtime.py

import datetime
import random

def time():
	d = datetime.datetime.now()
	y = d.year - 2000
	m = d.month
	dd = d.day
	h = d.hour
	me = d.minute
	s = d.second

	if h < 10:
		h = "0" + str(h)

	if me < 10:
		me = "0" + str(me)

	if s < 10:
		s = "0" + str(s)

	string = str(y) + "y" + str(m) + "m" + str(dd) + "d:" + str(h) + "h" + str(me) + "m" + str(s) + "s"
	
	return string

def Random():
	filename = time() #create the file and name it
	filename = filename + ".txt"
	f = open(filename, "a") #open the file (a represents the input of data to the end of the file)
	
	for i in range(0,65536):
		n = random.randint(65, 65+25)
		c = chr(n)
		f.write(c) #writes the result into the file
	f.close #close the file

def main():
	Random()
	
if __name__ == '__main__':
	main()
	
# text file will be the date and time when it was created.
#example: yearmonthday:hourminutesecond.txt
