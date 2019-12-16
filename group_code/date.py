# date.py

import datetime

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


print(string)
