import turtle
 
myTurtle = turtle.Turtle(shape="turtle")
 
myTurtle.penup()
myTurtle.setposition(0, 0)
myTurtle.pendown()
myTurtle.circle(25)
 
myTurtle.penup()
myTurtle.setposition(25, 0)
myTurtle.pendown()
myTurtle.circle(25)
 
myTurtle.penup()
myTurtle.setposition(-25, 0)
myTurtle.pendown()
myTurtle.circle(25)
 
myTurtle.penup()
myTurtle.setposition(0, 25)
myTurtle.pendown()
myTurtle.circle(25)

myTurtle.penup()
myTurtle.setposition(0, -25)
myTurtle.pendown()
myTurtle.circle(25)

 
turtle.getscreen()._root.mainloop()