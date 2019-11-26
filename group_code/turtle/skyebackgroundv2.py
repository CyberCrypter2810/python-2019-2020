#skyebackground v2
#JSkye, JTP TECH 2019
import turtle

def draw_default(screenx,screeny,t):
	t.speed(0)
	t.penup()
	
	screenxpos = screenx * -1
	screenypos = screeny * -1
	screenxpos2 = screenx * 2
	screenypos2 = screeny * 2
	
	
	#screenx = screen
	
	t.goto(screenxpos,screenypos)
	t.pendown()
	t.fillcolor("#A1E1FF")
	t.begin_fill()
	if (screenx > screeny):
		t.forward(screenxpos2)
		t.left(90)
		t.forward(screenxpos2)
		t.left(90)
		t.forward(screenxpos2)
		t.left(90)
		t.forward(screenxpos2)
		

	elif (screenx < screeny):
		#deb("Y is bigger than X drawing Y...")
		t.forward(screenypos2)
		t.left(90)
		t.forward(screenypos2)
		t.left(90)
		t.forward(screenypos2)
		t.left(90)
		t.forward(screenypos2)

	else:
		t.forward(screenypos2)
		t.left(90)
		t.forward(screenypos2)
		t.left(90)
		t.forward(screenypos2)
		t.left(90)
		t.forward(screenypos2)
		
	
	

	t.end_fill()
	t.penup()

#---------------------------------------------------------


def rocks(screenx, screeny, t):

	t.pencolor("#4689A8")
	#t.begin_fill()
	t.pensize(10)
	t.speed(5)
	screenxpos = screenx * -1
	screenypos = screeny * -1
	screenxpos2 = screenx * 2
	screenypos2 = screeny * 2
	t.penup()
	
	t.goto(100,300)
	i = 0
	for i in range(8):
		
		t.pendown()
		
		t.forward(1)
		t.penup()
		t.forward(40)
		t.right(80)
		
		t.pencolor("#4689A8")
		t.pensize(17)
		
		t.pendown()
		t.forward(1)
		t.penup()
		t.forward(110)
		t.left(20)
		
		t.pencolor("#18485E")
		t.pensize(13)
		
		t.pendown()
		t.forward(3)
		t.penup()
		t.forward(70)
		t.right(50)
		
		t.pencolor("#A7A7A7")
		t.pensize(20)
		
		t.pendown()
		t.forward(7)
		t.penup()
		t.forward(20)
		t.left(50)

#-----ROUND 2

		t.pendown()
		
		t.forward(1)
		t.penup()
		t.forward(40)
		t.left(80)
		
		t.pencolor("#8F8FDB")
		t.pensize(17)
		
		t.pendown()
		t.forward(1)
		t.penup()
		t.forward(110)
		t.left(20)
		
		t.pencolor("#1C1CCF")
		t.pensize(13)
		
		t.pendown()
		t.forward(3)
		t.penup()
		t.forward(70)
		t.right(50)
		
		t.pencolor("#7843E7")
		t.pensize(20)
		
		t.pendown()
		t.forward(7)
		t.penup()
		t.forward(20)
		t.left(50)



		
		#t.end_fill()
	#end of sequence
#---------------------------------------------------------



def main(screenx, screeny, t):
	
	draw_default(screenx,screeny,t)
	rocks(screenx,screeny,t)
	
	
	
	
if __name__=='__main__':
	screeny = 700
	screenx = 1000

	t = turtle.Turtle()
	screen = turtle.Screen()
	t.speed(0)
	turtle.setup(screenx, screeny)



	main(screenx,screeny,t)
	turtle.exitonclick()
 
