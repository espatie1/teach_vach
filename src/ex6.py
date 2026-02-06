import turtle

def forward(a):
    delta = a // k
    turtle.dot()
    for j in range (0, delta+1):
        turtle.fd(k)
        turtle.dot()

k = 10
screen = turtle.Screen()
screen.setup (1920, 1080)
screen.tracer(0)
for i in range (0,4):
    forward(30*k)
    turtle.right(90)
    forward(40*k)
    turtle.right(90)
turtle.penup()
turtle.fd(20*k)
turtle.right(90)
turtle.fd(5*k)
turtle.right(90)
turtle.pendown()
for g in range(0,6):
    forward(10*k)
    turtle.right(90)
turtle.penup()
screen.update()
screen.mainloop()