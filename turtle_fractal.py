import turtle
from l_systems import L_system
from PIL import Image

class new_turtle: 

	position = []
	orientation = 0

	
	
	
cantor = L_system({'a': 'aba', 'b':'bbb'}, 'aaaa', 'ab')

timmy = turtle.Turtle()
window = turtle.Screen()

cantor.successor(11)

l_string = cantor.get_l_string()
timmy.hideturtle()
timmy.penup()
window.screensize(1000, 1000)
timmy.setpos(0, 0)
window.tracer(0, 0)
timmy.pendown()

for l in l_string:
	if l == 'a':
		timmy.right(27)
		timmy.forward(1)
	if l == 'b':
		timmy.left(10)

ts = timmy.getscreen()


ts.getcanvas().postscript(file="snowflake2.eps")

window.mainloop()
