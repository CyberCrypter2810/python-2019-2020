#MainDriver
import turtle
import skyebackgroundv2
import gabesturtlepart
import bhead
#import two 
#import three

	
def driver():
	w = turtle.Screen()
	screenx = 700
	screeny = 700 

	w.setup(screenx, screeny)
	w.clear()
	w.bgcolor("#ffffff")
	t = turtle.Turtle()
	skyebackgroundv2.main(screenx,screeny,t)
	gabesturtlepart.main1()
	bhead.mainb()
	
	w.exitonclick()

if __name__ == '__main__':
	driver()
	
'''
#apt install python3-tk
	


wn = turtle.Screen()   # create a turtle
t = turtle.Turtle()
t.color('green')      # set the color
t.forward(50)         # draw a green line of leng
t.up()                # lift up the tail
t.forward(50)         # move forward 50 without drawing
t.right(90)           # change direction to the right, left works too
t.down()              # put the tail down
t.backward(100)       # draw a green line 100 units long
wn.exitonclick()
'''
