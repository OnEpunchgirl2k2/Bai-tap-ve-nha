import turtle

def drawCircle(x, y, radius = 50):
    myTurtle = turtle.Turtle()
    myTurtle.setposition(x, y)
    myTurtle.circle(radius)
    turtle.getscreen()._root.mainloop()

drawCircle(0, 0)