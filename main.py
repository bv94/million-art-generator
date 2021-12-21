import colorgram
from turtle import Turtle, Screen

colors = colorgram.extract('/storage/python project/million dollar color/image.jpg', 40)
colors.extend(colorgram.extract('/storage/python project/million dollar color/download.jpeg', 40))
colors.extend(colorgram.extract('/storage/python project/million dollar color/imgz.jpg', 40))

rgb_color = []
for color in colors:
	r = color.rgb.r
	b = color.rgb.b
	g = color.rgb.g
	rgb_color.append((r, g, b))
print(rgb_color)

turt = Turtle()
screen = Screen()
screen.colormode(255)


def start_action():
	turt.setheading(225)
	turt.forward(222)
	turt.setheading(0)


def new_line(gap, dot_count):
	turt.setheading(90)
	turt.forward(gap)
	turt.setheading(0)
	turt.backward(gap * dot_count)


ix = 0


def dotting(gap):
	global ix
	for i in range(100):
		turt.pencolor(rgb_color[i])
		turt.dot()
		turt.forward(gap)
		ix += 1
		if ix == 10:
			ix = 0
			new_line(gap, 10)


def dotter(gap, width):
	turt.penup()
	start_action()
	turt.width(width)
	dotting(gap)


dotter(40, 6)
screen.exitonclick()
