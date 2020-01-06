import turtle
import math
wdth = 800; hgth = 800; bgstring = "#ffffff"
red = "#cc0000"; green = "#00cc00"; blue = "#0000cc"

def grid(t):
	x = 0; y = 0
	while (x < 400):
		t.color(green)
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x,y+400)
		x = x + 50
	x = 0; y = 0
	while (y < 400):
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x+400,y)
		y = y + 50
	t.color('orange')
	style = ('Courior', 20, 'bold')
	t.write('Circle Circumference and Diameter', font=style, align='right')
	t.penup()
	t.goto(150,-50)
	t.pendown()
	t.write('Diameter', font=style, align='left')
	t.penup()
	t.goto(-130,180)
	t.pendown()
	t.write('Circumference', font=style, align='center')
	t.penup()

def plotCircles(t):
	d =  [12.8, 1.8, 19.8, 8.7] 
	c =  [3*12.8,  3*1.8, 3*19.7, 3* 8.7] 
	dsorted = sorted (d, key = float)
	csorted = sorted(c , key = float)
	t.goto(0,0)
	t.color(red)
	t.pendown()
	t.dot(3, blue)
	t.goto(dsorted[0],csorted[0])
	t.dot(3, blue)
	t.goto(dsorted[1],csorted[1])
	t.dot(3, blue)
	t.goto(dsorted[2],csorted[2])
	t.dot(3, blue)
	t.goto(dsorted[3],csorted[3])
	t.dot(3, blue)
	
def main():
	try:
		turtle.TurtleScreen._RUNNING = True
		# get wdth and hgth globally
		turtle.screensize(canvwidth=wdth, canvheight=hgth, bg=bgstring)
		print(turtle.Screen().screensize())
		w = turtle.Screen()
		t = turtle.Turtle()
		t.hideturtle()
		grid(t)
		plotCircles(t)
		w.exitonclick()
	finally:
		turtle.Terminator()
	
if __name__ == '__main__':
	main()
