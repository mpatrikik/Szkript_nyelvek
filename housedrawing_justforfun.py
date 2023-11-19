# draw a house
# using the turtle module

# import the turtle module
import turtle

# create a turtle object
my_turtle = turtle.Turtle()

# draw a house
my_turtle.speed(7)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(180)
my_turtle.forward(100)
my_turtle.right(45)
my_turtle.forward(70)
my_turtle.right(90)
my_turtle.forward(70)
my_turtle.penup()
my_turtle.goto(65, 0)
my_turtle.pendown()
my_turtle.left(135)
my_turtle.forward(25)
my_turtle.right(90)
my_turtle.forward(15)
my_turtle.right(90)
my_turtle.forward(25)


# keep the window open
turtle.done()
