import turtle

turtle.speed(0)
turtle.hideturtle()

color="black"

def color_red():
    global color
    color="red"
def color_black():
    global color
    color="black"
def color_purple():
    global color
    color="purple"
def draw_circle(color,x,y):
    turtle.begin_fill()
    turtle.color(color)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(20)
    turtle.end_fill()
    turtle.penup()
def circle(x,y):
    global color
    draw_circle(color,x,y)


turtle.getscreen().onkeypress(color_red,"r")
turtle.getscreen().onkeypress(color_black,"b")
turtle.getscreen().onkeypress(color_purple,"p")
turtle.onscreenclick(circle)
#turtle.onscreenclick(blue_circle,btn=3)

#draw_circle("blue",70,20)


def draw_square(color,x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.color(color)
    turtle.pendown()
    turtle.goto(x+50,y)
    turtle.goto(x+50,y+50)
    turtle.goto(x,y+50)
    turtle.end_fill()
    turtle.penup()
def square(x,y):
    global color
    draw_square(color,x,y)
turtle.onscreenclick(square,btn=3)


turtle.getscreen().listen()

  
turtle.mainloop()
