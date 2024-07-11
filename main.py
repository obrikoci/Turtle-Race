from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()
screen.setup(500, 400)
user_bet =  screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter your color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -100, -50, 0, 50, 100 ]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
    
if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle won the race. ")
            else:
                print(f"You lost! The {winning_color} turtle won the race.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()