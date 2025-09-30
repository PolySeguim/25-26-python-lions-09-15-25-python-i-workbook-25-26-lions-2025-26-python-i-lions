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

def spiral():
    poly.circle(50)

draw_clock()

screen.listen()
screen.mainloop()