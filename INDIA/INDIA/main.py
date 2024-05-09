import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("INDIAN MAP")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)
indian_states = pandas.read_csv("indian_states.csv")
states_list = indian_states["state"].tolist()
guessed_states_list = []
while len(states_list) < 28:
    guess_state = screen.textinput(title="Guess a state", prompt= "Guess the indian state").title()
    if guess_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states_list]
        missing_states_file = pandas.DataFrame(missing_states)
        missing_states_file.to_csv("states_to_learn.csv")
        break
    if guess_state in states_list:
        turtle = Turtle()
        turtle.penup()
        turtle.hideturtle()
        turtle.color("red")
        selected_state_data = indian_states[indian_states["state"] == guess_state]
        x = int(selected_state_data["x"])
        y = int(selected_state_data["y"])
        turtle.goto(x,y)
        turtle.write(guess_state)
        guessed_states_list.append(guess_state)
screen.exitonclick()

turtle.mainloop()

