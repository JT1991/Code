import turtle

def draw_triangle(some_turtle):
    turns_made = 0
    turns_square = 3
    while (turns_made < turns_square):
        some_turtle.forward(100)
        some_turtle.left(120)
        turns_made += 1
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("brown")
    
    #instance of turtle to write initals
    author = turtle.Turtle()
    author.color("blue")
    author.hideturtle()
    author.penup()
    author.goto(200,-100)
    author.write('J.T', move=False, align="left",font=('Arial',40,'normal'))
    
    #instance of turtle - drawing a square (uses function draw_square)
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(10)
    brad.color("red")
    for i in range(1,37):
        draw_triangle(brad)
        brad.right(10)
        if i in range(-1,5):
            brad.color("orange")
        if i in range(5,10):
            brad.color("red")
        if i in range(10,17):
            brad.color("orange")
        if i in range(17,22):
            brad.color("red")
        if i in range(22,28):
            brad.color("orange")
        if i in range(28,37):
            brad.color("red")
    brad.right(90)
    brad.color("green")
    brad.forward(300)
    
    #instance of turtle- drawing circle
   # angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.circle(100)
    #angie.color("blue")
   
    window.exitonclick()
draw_art()
