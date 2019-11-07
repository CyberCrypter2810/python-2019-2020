import turtle

def eyes(p):
	p.goto(5,17)
	#p.hideturtle()
	p.down()
	p.begin_fill()
	p.color('black')
	for i in range (1):
		p.circle(1,360)
		p.lt(90)
	p.end_fill()
	p.up()
	#p.showturtle()
	p.goto(-6,17)
	p.rt(90)
	p.down()
	#p.hideturtle()
	p.begin_fill()
	for i in range (1):
		p.circle(1,360)
		p.rt(90)
	p.end_fill()


def halfcircle(p):
	p.up()
	p.goto(10,10)
	p.lt(90)
	#p.hideturtle()
	p.down()
	p.begin_fill()
	p.color('green')
	for i in range(1):
		p.circle(10,180)
		p.lt(90)
		p.forward(20)
	p.end_fill()
	p.up()
	#p.showturtle()
	
def head(p):
	halfcircle(p)
	eyes(p)

def mainb():
	w = turtle.Screen()
	#w.setup(700, 700)
	#w.clear()
	#w.bgcolor("white")
	p = turtle.Turtle()
	head(p)
	w.exitonclick()
	
if __name__ == '__main__':
	mainb()
