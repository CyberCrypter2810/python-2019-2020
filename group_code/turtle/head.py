import turtle

def eyes(t):
	t.goto(15,25)
	t.hideturtle()
	t.down()
	t.begin_fill()
	t.color('black')
	for i in range (1):
		t.circle(5,360)
		t.lt(90)
	t.end_fill()
	t.up()
	t.showturtle()
	t.goto(-35,25)
	t.rt(90)
	t.down()
	t.hideturtle()
	t.begin_fill()
	for i in range (1):
		t.circle(5,360)
		t.rt(90)
	t.end_fill()


def halfcircle(t):
	t.up()
	t.goto(40,0)
	t.lt(90)
	t.hideturtle()
	t.down()
	t.begin_fill()
	t.color('green')
	for i in range(1):
		t.circle(50,180)
		t.lt(90)
		t.forward(100)
	t.end_fill()
	t.up()
	t.showturtle()
	
def head(t):
	halfcircle(t)
	eyes(t)

def main():
	w = turtle.Screen()
	w.setup(700, 700)
	w.clear()
	w.bgcolor("white")
	t = turtle.Turtle()
	head(t)
	w.exitonclick()
	
if __name__ == '__main__':
	main()
