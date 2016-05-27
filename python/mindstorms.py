import turtle

def draw_square(some_turtle):
    turns_made = 0
    turns_square = 4
    while (turns_made < turns_square):
        some_turtle.forward(100)
        some_turtle.right(90)
        turns_made += 1
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #instance of turtle - drawing a square (uses function draw_square)
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(10)
    brad.color("green")
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #instance of turtle- drawing circle
   # angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.circle(100)
    #angie.color("blue")
   
    window.exitonclick()
draw_art()
