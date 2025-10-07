import turtle

screen = turtle.Screen()
screen.bgcolor("white")

#global variable
poly = turtle.Turtle()
poly.color("green")

def draw_clock():
    poly.stamp()
    #loop variable
    #meaning that the i will be 1,2,3,4,5,6,7,...12
    for i in range(12):
        poly.penup() #poly.pu()
        poly.forward(150)
        poly.pendown()
        poly.stamp()
        poly.penup()
        poly.backward(150)
        poly.pendown()
        poly.left(30)

def draw_clock(t):
#def draw_clock(Turtle t)
    t.stamp()
    #loop variable
    #meaning that the i will be 1,2,3,4,5,6,7,...12
    for i in range(12):
        t.penup() #poly.pu()
        t.forward(150)
        t.pendown()
        t.stamp()
        t.penup()
        t.backward(150)
        t.pendown()
        t.left(30)

def square_spiral():
    distance = 3
    poly.speed(100)
    for i in range(500):
        poly.forward(distance)
        poly.right(90)
        distance = distance + 3

def square_spiral2():
    distance = 3
    poly.speed(100)
    for i in range(500):
        poly.forward(distance)
        poly.right(89)
        distance = distance + 1

# t is an instantiation of the Turtle object
# sz is an integer datatype to determine the size of your square.
def draw_multicolor_square(t, sz, colors):
    """Make turtle t draw a multi-color square of sz."""
    t.pensize(getThickness())
    for i in colors:
        t.color(i)
        t.forward(sz)
        t.left(90)

def getThickness():
    thickness = int(input("Enter the thickness of the turtle"))
    return thickness

def draw_square(t, side):
    for i in range(4):
        t.forward(side)
        t.right(90)

def draw_multiple_squares(t, side, num):
    for i in range(num):
        draw_square(t, side)
        t.penup()
        t.forward(side*2)
        t.pendown()

#TEST SUITE
def test():
    test_turtle = turtle.Turtle()
    test_turtle.color("hotpink")
    #draw_square(test_turtle, 20)
    draw_multiple_squares(test_turtle, 20, 5)
#Us calling the test suite
test()

#turtle.done()
screen.listen()
screen.mainloop()


#draw_clock() # without a parameter
#draw_clock(test_turtle) # with a turtle parameter
#color1 = ["red", "purple", "hotpink", "blue"]
#color2 = ["black", "orange", "green", "yellow"]
#color3 = ["purple", "red", "gray", "brown"]
#draw_multicolor_square(test_turtle, 20, color1)
#draw_multicolor_square(test_turtle, 50, color2)
#draw_multicolor_square(test_turtle, 100, color3)