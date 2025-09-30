import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

poly = turtle.Turtle()
poly.color("blue")

def draw_clock():
    poly.stamp()
    for i in range(12):
        poly.penup() #poly.pu()
        poly.forward(150)
        poly.pendown()
        poly.stamp()
        poly.penup()
        poly.backward(150)
        poly.pendown()
        poly.left(30)

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


#draw_clock()
#square_spiral()
square_spiral2()


screen.listen()
screen.mainloop()