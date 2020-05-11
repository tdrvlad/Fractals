import graphics
import random
import time
import sys

#________________Parameters________________

scale = 500
start_triangle = ((1,1),(0.5,0),(0,1))  #Coordinates are in mirror

win=graphics.GraphWin("Figure",scale,scale)
win.setBackground("white")
colour=graphics.color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))


#________________Parameters________________

def draw_triangle(colour,points_coord):
	vertices = []
	for i in range(3):  
		(x,y) = points_coord[i]                       # Do this 3 times
		vertices.append(graphics.Point(scale * x, scale * y)) # Add the (x, y) point to the vertices
	triangle = graphics.Polygon(vertices)
	triangle.setFill(colour)
	triangle.draw(win)

	return triangle


def undraw_triangle(triangle):
	triangle.undraw()
	return 1


def triangle_to_vertices(triangle):	
	vertices = triangle.getPoints()
	points =()
	for vertice in vertices:
		x = vertice.getX() / scale
		y = vertice.getY() / scale
		points += ((x, y),)
	
	return points
	
	
def sierpinsky_ieration(existing_triangles):
	
	new_triangles = []
	for triangle in existing_triangles:

		vertices = triangle_to_vertices(triangle)

		undraw_triangle(triangle)

		no_vertices = len(vertices)
		mid = ()
		for i in range(no_vertices):
			(x1,y1) = vertices[i]
			(x2,y2) = vertices[(i + 1) % no_vertices] 
			mid += ( ( min(x1,x2) + (max(x1,x2) - min(x1,x2)) / 2, min(y1,y2) + (max(y1,y2) - min(y1,y2)) / 2 ), ) #Calculating the coordintates of the midpoint of the 2 points
		
		for i in range(no_vertices):	
			new_triangle = (vertices[i],mid[i],mid[(i-1)%no_vertices])
			new_triangles.append(draw_triangle(colour,new_triangle))

		'''
		Equivalent to:
		(x0,y0),(x1,y1),(x2,y2) = triangle_to_vertices(triangle)

		mid01 = (x0 + (x1-x0)/2, y0 + (y1 - y0)/2)
		mid02 = (x0 + (x2-x0)/2, y0 + (y2 - y0)/2)
		mid12 = (x1 + (x2-x1)/2, y1 + (y2 - y1)/2)
		
		new_triangle = ((x0,y0),mid01,mid02)
		new_triangles.append(draw_triangle(colour,new_triangle))

		new_triangle = (mid02,mid12,(x2,y2))
		new_triangles.append(draw_triangle(colour,new_triangle))

		new_triangle = (mid01,(x1,y1),mid12)
		new_triangles.append(draw_triangle(colour,new_triangle))
		'''
		undraw_triangle(triangle)

	return new_triangles


def sierpinsky_triangle(no_generations):
	
	triangles = []
	
	triangles.append(draw_triangle(colour,start_triangle))

	for i in range(no_generations):
		time.sleep(1.5)
		triangles = sierpinsky_ieration(triangles)


#________________Run________________

number_of_iterations = int((sys.argv)[1])
print(number_of_iterations)
sierpinsky_triangle(number_of_iterations)
win.getMouse()
win.close()