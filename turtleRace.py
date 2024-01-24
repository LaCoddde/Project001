import random
from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width=500, height=400)  # Allows to set up screen width and height
user_bet = my_screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
# Line above brings a pop-up screen for user to give sting input.
print(user_bet.title())

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False

# Create multiple turtles
# timmy = Turtle()
# timmy.penup()
# timmy.shape("turtle")
# timmy.color(colours[0])
# timmy.goto(x=-230, y=-150)
#
# tommy = Turtle(shape="turtle")
# tommy.penup()
# tommy.color(colours[1])
# tommy.goto(x=-230, y=-100)
#
# jenny = Turtle(shape="turtle")
# jenny.penup()
# jenny.color(colours[2])
# jenny.goto(x=-230, y=-50)
#
# sammy = Turtle(shape="turtle")
# sammy.penup()
# sammy.color(colours[3])
# sammy.goto(x=-230, y=0)
#
# benny = Turtle(shape="turtle")
# benny.penup()
# benny.color(colours[4])
# benny.goto(x=-230, y=50)
#
# johnny = Turtle(shape="turtle")
# johnny.penup()
# johnny.color(colours[5])
# johnny.goto(x=-230, y=100)

y_position = [-150, -100, -50, 0, 50, 100]
all_turtles = []
winning_color = ""

for item in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[item])
    new_turtle.goto(x=-230, y=-y_position[item])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for item in all_turtles:
        if item.xcor() > 230:  # if turtle x coordinate > 230. ( 250 - (40/2) ) turtle is 40 pixel wide
            is_race_on = False
            winning_color = item.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle wins.")
            else:
                print(f"You've lost! The {winning_color} turtle wins.")
        rand_distance = random.randint(0, 10)
        item.forward(rand_distance)

my_screen.exitonclick()
