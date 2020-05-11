import graphics
import random
import time
import sys
import math

#________________Parameters________________

scale = 700
border = 0.2
height = math.sqrt(3)/2
start_triangle = ((1 - border, 1 - border),(0.5, 1 - height),(border, 1 - border)) #Coordineates in mirror

win=graphics.GraphWin("Figure",scale,scale)
win.setBackground("white")
colour=graphics.color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))


#________________Parameters________________

def draw_triangle(colour,points_coord):
	vertices = []
	for i in range(3):  
		(x,y) = points_coord[i]                       # Do this 3 times
		vertices.append(graphics.Point(scale * x, scale * y)) # Add the (x, y) point to the vertices
	
	lines = []
	for i in range(3):
		line = graphics.Line(vertices[i],vertices[(i +1 ) % 3])
		line.draw(win)
		lines.append(line)
	
	return lines

def draw_line(colour,points_coord):
	vertices = []
	for i in range(2):  
		(x,y) = points_coord[i]                   # Do this 2 times
		vertices.append(graphics.Point(scale * x, scale * y))# Add the (x, y) point to the vertices

	line = graphics.Line(vertices[0],vertices[1])
	line.draw(win)

	return line


def undraw_line(line):
	line.undraw()
	return 1


def line_to_vertices(line):	
	vertices = [line.getP1(),line.getP2()]
	points =()
	for vertice in vertices:
		x = vertice.getX() / scale
		y = vertice.getY() / scale
		points += ((x, y),)
	
	return points
	
	
def koch_iteration(existing_lines):
	
	new_lines = []
	for line in existing_lines:

		vertices = line_to_vertices(line)

		no_vertices = len(vertices)

		(xa,ya) = vertices[0]
		(xb,yb) = vertices[1] 

		x1 = xa + (xb - xa) / 3
		x2 = xa + (xb - xa) * 2 / 3

		y1 = ya + (yb - ya) / 3
		y2 = ya + (yb - ya) * 2 / 3

		cos60 = 0.5
		sin60 = math.sqrt(3) / 2

		x3 = x1 + cos60 * (x2 - x1) - sin60 * (y2 - y1)
		y3 = (y1 + sin60 * (x2 - x1) + cos60 * (y2 - y1))

		new_line = ((xa,ya),(x1,y1))
		new_lines.append(draw_line(colour,new_line))

		new_line = ((x1,y1),(x3,y3))
		new_lines.append(draw_line(colour,new_line))

		new_line = ((x3,y3),(x2,y2))
		new_lines.append(draw_line(colour,new_line))

		new_line = ((x2,y2),(xb,yb))
		new_lines.append(draw_line(colour,new_line))

		undraw_line(line)

	return new_lines


def koch_curve(no_generations):
	
	lines = []
	lines += draw_triangle(colour,start_triangle)

	print(lines)
	for i in range(no_generations):
		time.sleep(1.5)
		lines = koch_iteration(lines)


#________________Run________________

number_of_iterations = int((sys.argv)[1])
print(number_of_iterations)
koch_curve(number_of_iterations)
win.getMouse()
win.close()