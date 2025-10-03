import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

#global variable
poly = turtle.Turtle()
poly.color("blue")

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


#TEST SUITE
def test():
    test_turtle = turtle.Turtle()
    test_turtle.color("pink")
    draw_clock() # without a parameter
    draw_clock(t) # with a turtle parameter

    #draw_clock()
    #square_spiral()
    #square_spiral2()

#Us calling the test suite
test()

turtle.done()
screen.listen()
screen.mainloop()