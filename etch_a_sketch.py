from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_lef():
    tim.setheading(tim.heading() + 10)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen = Screen()
screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_lef)
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
