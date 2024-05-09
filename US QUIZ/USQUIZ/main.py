import turtle
from  turtle import Turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
correct_guesses = []
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title= f"{score}/50", prompt="Guess the states name?").title()
    states_data = pandas.read_csv("50_states.csv")
    all_states = states_data["state"].tolist()
    if answer_state == "Exit":
        # missing_states = []
        missing_states = [state for state in states_list if state not in guessed_states_list]
        missing_data = pandas.DataFrame(missing_states)
        missing_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        score += 1
        correct_guesses.append(answer_state)
        turtle = Turtle()
        turtle.color("red")
        turtle.hideturtle()
        turtle.penup()
        current_state_data = states_data[states_data["state"] == answer_state]
        x_pos = int(current_state_data["x"])
        y_pos = int(current_state_data["y"])
        turtle.goto(x_pos, y_pos)
        turtle.write(answer_state)

    else:
        pass
