from turtle import *

#we want to paint a house

#step 1:  draw a spuare 
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of spuare 

#drawing a door 

forward(70)
color("yellow")
left(90)
forward(120)     #height of the door 
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("blue")
penup()
goto(200, 150)
pendown()
right(60)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
goto(0, 150)
pendown()
forward(50)
right(90)
forward(50)
right(90)
forward(50)



exitonclick()