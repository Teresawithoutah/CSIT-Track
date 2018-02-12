from turtle import *

edge = pencolor('#BF5252')
inside = fillcolor('#F9E30E')

begin_fill()
def drawPolygonFilled(sides,edge,inside):
    for i in range(sides):  
        forward(200)
        right(90)
 
drawPolygonFilled(4,edge,inside)
end_fill()
